from sys import stdin

def maximum_gold(capacity, weights):
    ## build cache
    cache = [[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]

    ## build optimal weights row-wise.
    ## Each row shows the optimal weight of the items up to that point (i.e. in row 2, i only consider the first 2 elements)
    for row in range(1, len(weights)+1):
        for col in range(1, capacity+1):
            # print('='*50)
            # print(row, col)
            # display(cache)
            if col < weights[row-1]:
                cache[row][col] = cache[row-1][col]
            else:
                cache[row][col] = max(
                    cache[row-1][col-weights[row-1]] + weights[row-1],
                    cache[row-1][col]
                )

    ## return bottom right
    return cache[len(weights)][capacity]

if __name__ == '__main__':
    # input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    input_capacity, n = list(map(int, input().split()))
    input_weights = list(map(int, input().split()))
    
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
