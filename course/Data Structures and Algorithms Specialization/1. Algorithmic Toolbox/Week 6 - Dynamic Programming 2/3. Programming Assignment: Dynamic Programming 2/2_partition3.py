# from sys import stdin

def partition3(values, partition_count=3, verbose=False):
    total_sum = sum(values)
    if total_sum % partition_count != 0:
        return 0
        
    partition_value_target = total_sum/partition_count
    # values = sorted(values, reverse=True)
    partition_values = [0] * partition_count

    ## Each queue element represents (`value_index`, `partition_index`)
    queue = [(0, 0)]
    success = []
    total_succeed = 0
    i = 0
    while queue:
        i+=1
        if verbose:
            print('='*50)
            print(f"{queue=}, {success=}, {partition_values=}, {total_succeed=}, {i=}")

        value_index, partition_index = queue.pop()
        if value_index >= len(values):
            return 1

        if ((partition_values[partition_index] + values[value_index]) <= partition_value_target):
            if verbose:
                print(f'Successfully adding {value_index=}, {partition_index=}')
            partition_values[partition_index] += values[value_index]
            queue.append((value_index+1, 0))
            success.append((value_index, partition_index))
            if partition_values[partition_index] == partition_value_target:
                total_succeed += 1
        else:
            if verbose:
                print(f'Unable to add {value_index=}, {partition_index=}')
            at_partition_end = (partition_index+1) >= partition_count
            
            # Otherwise, try the current value in the next partition
            if not at_partition_end:
                if verbose:
                    print(f'Trying ({value_index=}, {partition_index+1=})')
                queue.append((value_index, partition_index+1))
            else:
                # If we are at the end of either the values or the partitions arrays, backtrack to last success
                if verbose:
                    print('At partition end')
                while at_partition_end:
                    try:
                        value_index, partition_index = success.pop()
                    except:
                        return 0
                    
                    if verbose:
                        print(f'Backtracking to ({value_index=}, {partition_index=})')
                    
                    if partition_values[partition_index] == partition_value_target:
                        total_succeed -= 1
                    
                    partition_values[partition_index] -= values[value_index]
                    
                    at_partition_end = (partition_index+1) >= partition_count
                    
                    ## If we have backtracked to the point where a partition value is 0, that means that no combination of values (from and including this value to the end) can give the desired value. 
                    ## Take for example the [4,4,2] subarray in [3,1,1,4,4,2]. 
                    ##  State: [5, 0, 0] 
                    ##  Target value: 5
                    ##  Subarray: [4,4,2]
                    ## We know that this is bound to fail. But before it fails, we must have tried 4+4, 4+2, 4+2 (that is, a+b, a+c, b+c)
                    ## Then, once all combinations are tried, there is no need to worry about the cases (b+a, c+a, c+b) by symmetry. So if we backtrack till a 0 is hit, break the iteration
                    if partition_values[partition_index] == 0:
                        at_partition_end = True

                queue.append((value_index, partition_index+1))
        
        if total_succeed >= (partition_count-1):
            return 1

if __name__ == '__main__':
    # input_n, *input_values = list(map(int, stdin.read().split()))
    input_n = input()
    input_values = list(map(int, input().split()))
    
    assert int(input_n) == len(input_values)
    print(partition3(input_values))
