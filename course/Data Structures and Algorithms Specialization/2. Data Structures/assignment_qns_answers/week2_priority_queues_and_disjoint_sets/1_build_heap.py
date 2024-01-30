# python3

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return 
    
def left_child(input_list, index):
    child_index = (2*index) + 1
    if child_index < len(input_list):
        return child_index 
    else:
        return index

def right_child(input_list, index):
    child_index = (2*index) + 2
    if child_index < len(input_list):
        return child_index 
    else:
        return index

def parent(input_list, index):
    return (index-1)//2

def sift_down(input_list, index):
    curr_index = index
    swaps = []

    while (input_list[curr_index] > input_list[left_child(input_list, curr_index)]) or (input_list[curr_index] > input_list[right_child(input_list, curr_index)]):  
        # print(f"sift_down: {curr_index=}, {input_list=}, {left_child(input_list, curr_index)=}, {right_child(input_list, curr_index)=}")
        swap_index = left_child(input_list, curr_index) if input_list[left_child(input_list, curr_index)] < input_list[right_child(input_list, curr_index)] else right_child(input_list, curr_index)

        input_list[curr_index], input_list[swap_index] = input_list[swap_index], input_list[curr_index]
        swaps.append((curr_index, swap_index))
        
        curr_index = swap_index
        # print(f"sift_down: {input_list=}")
    return swaps

def heapify(input_list):
    start_index = len(input_list)//2
    swaps = []
    for index in range(start_index, -1, -1):
        # print(f"Heapify: {index=}, {input_list=}")
        additional_swaps = sift_down(input_list, index)
        swaps.extend(additional_swaps)
        # print(f"Heapify: {index=}, {input_list=}")
    
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = heapify(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
