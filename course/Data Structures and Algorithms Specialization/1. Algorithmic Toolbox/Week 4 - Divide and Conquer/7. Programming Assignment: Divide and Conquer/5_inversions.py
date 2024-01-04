from itertools import combinations


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def inversions_binary(a, count_inversions = 0):
    '''
    Time complexity: 
    Space complexity:
    '''
    mid = len(a)//2
    if len(a) == 1:
        return a, 0

    left_array, count_invs_left = inversions_binary(a[:mid], count_inversions)
    right_array, count_invs_right = inversions_binary(a[mid:], count_inversions)
    sorted_array = []
    count_inversions = count_invs_left + count_invs_right

    while (len(left_array) != 0) & (len(right_array) != 0):
        if left_array[0] <= right_array[0]:
            sorted_array.append(left_array.pop(0))
        else:
            sorted_array.append(right_array.pop(0))
            count_inversions += len(left_array)

    if len(left_array) != 0:
        sorted_array.extend(left_array)
    
    if len(right_array) != 0:
        sorted_array.extend(right_array)

    return sorted_array, count_inversions

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_binary(elements)[1])
