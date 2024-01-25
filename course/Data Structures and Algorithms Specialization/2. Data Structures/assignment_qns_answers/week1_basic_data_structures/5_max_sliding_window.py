# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

def window_max(input_list, window_size, verbose=False):
    '''
    Time complexity O(N): 
        - O(N) from iterating through each element of the input list. For each element, a fixed number of comparisons are made. 
        - At most k comparisons from both while loops

        - Taken together, it may seem like O(NK)
        - But notice that every element in the deque is added only once and popped only once. So the `while` loop is actually amortized O(N)
        - As such, time complexity is O(N)
    Space complexity O(N):
        - Storing the deque takes O(K) space in the worst case (since we are constantly popping items that are outside the window)
    '''
    maxval_index_deque = deque()
    output_index = 0
    output_list = []

    for i in range(len(input_list)):
        if verbose:
            print('='*50)
            print(f"{i=}, {maxval_index_deque=}, {output_list=}")
            if maxval_index_deque:
                print(f"{[input_list[x] for x in maxval_index_deque]=}")
        
        ## If the deque is not empty, remove all values smaller than the current input, starting from left of deque. 
        ## Because of the 2 while loops, the deque arranged from small to large going from left to right
        ## As such, it is guaranteed that indices i+1... after index i must be larger than index i
        ## So if we stop popping from maxval_index_deque, there is no need to check the subsequent values
        while (maxval_index_deque) and (input_list[maxval_index_deque[0]] < input_list[i]):
            maxval_index_deque.popleft()

        ## If the deque is not empty, remove all values outside the window of interest, starting from the right; that is, going from large to small. 
        ## Why right to left?
            ## At every step of the loop, we remove values outside the relevant window, and we remove all values that are smaller than the latest addition
            ## So it stands to reason that 
                ## (i) either the latest addition is the current max, and there are no other values in the deque
                ## or (ii) the latest value is not the current max, and the current maximum occurred somewhere before the latest added index
                ## As such, we should expect that the deque must be of strictly decreasing order, because there is never a case where we append a larger index to the right
        while (maxval_index_deque) and (maxval_index_deque[-1] <= (i-window_size)):
            maxval_index_deque.pop()

        ## Having done the above preocessing, append the latest index on the left
        maxval_index_deque.appendleft(i)

        ## Starting from the `window_size-1`-th index, every run of the loop is a possible window. Hence, we return the maximum value of the window by taking the rightmost value in the deque
        if i >= (window_size-1):
            output_list.append(input_list[maxval_index_deque[-1]])

        if verbose:
            print(f"{i=}, {maxval_index_deque=}, {output_list=}")
            if maxval_index_deque:
                print(f"{[input_list[x] for x in maxval_index_deque]=}")

    return output_list

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*window_max(input_sequence, window_size))

