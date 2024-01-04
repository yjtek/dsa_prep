from random import randint

def partition3(array, left, right):
    end_of_left_array = left+1
    start_of_right_array = right
    curr_index = left+1

    while curr_index <= start_of_right_array:
        # print(f"{array=}, {curr_index=}")
        if array[curr_index] < array[left]:
            array[curr_index], array[end_of_left_array] = array[end_of_left_array], array[curr_index]
            end_of_left_array += 1
            curr_index += 1
        elif array[curr_index] > array[left]:
            array[curr_index], array[start_of_right_array] = array[start_of_right_array], array[curr_index]
            start_of_right_array -= 1
        elif array[curr_index] == array[left]:
            curr_index += 1
    return end_of_left_array, start_of_right_array

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
