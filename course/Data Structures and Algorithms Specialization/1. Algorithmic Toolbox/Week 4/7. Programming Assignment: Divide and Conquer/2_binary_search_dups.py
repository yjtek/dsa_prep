def binary_search(keys, query):

    ## init left and right pointers
    left = 0
    right = len(keys)-1
    retval = -1

    while left <= right:
        # print(f"{left=}, {right=}")
        mid = (left+right)//2
        if keys[mid] == query:
            retval = mid
            right=mid-1
        elif keys[mid] > query:
            right=mid-1
        elif keys[mid] < query:
            left=mid+1
    
    return retval


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
