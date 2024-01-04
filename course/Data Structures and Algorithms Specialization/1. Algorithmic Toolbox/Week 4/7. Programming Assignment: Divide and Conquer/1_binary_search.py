def binary_search_recursive(keys, query, left, right):
    index = -1
    mid = (left+right)//2

    if keys[mid] == query:
        return mid

    if left >= right:
        return -1

    if keys[mid] < query:
        left = mid+1
        return binary_search_recursive(keys, query, left, right)
     
    if query < keys[mid]:
        right = mid-1
        return binary_search_recursive(keys, query, left, right)

def binary_search_iterative(keys, query):
    left = 0
    right = len(keys)

    while left < right:
        mid = (left+right)//2

        if keys[mid] == query:
            return mid
        elif keys[mid] < query:
            left = mid+1
        elif keys[mid] > query:
            right = mid-1
    
    return -1


def binary_search(keys, query):
    return binary_search_recursive(keys, query, 0, len(keys)-1)

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
