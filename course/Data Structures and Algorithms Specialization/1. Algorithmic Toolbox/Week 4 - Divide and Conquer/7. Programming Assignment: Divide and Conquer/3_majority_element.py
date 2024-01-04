def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def majority_moores(input_array):
    '''
    Time complexity: O(N) for the initial loop, and another O(N) for the second loop, for an overall O(N)
    Space complexity: O(1), because constant data is stored
    '''

    majority_element = None
    count_majority_excess = 0
    for elem in input_array:
        if count_majority_excess == 0:
            majority_element = elem
            count_majority_excess += 1
        elif elem == majority_element:
            count_majority_excess += 1
        elif elem != majority_element:
            count_majority_excess -= 1
    
    check_majority = 0
    for elem in input_array:
        if elem == majority_element:
            check_majority += 1
    
    if check_majority >= ((len(input_array)//2)+1):
        return 1
    else:
        return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    # print(majority_element_naive(input_elements))
    print(majority_moores(input_elements))
