'''
The h-index is a metric used to measure the impact and productivity of a scientist or researcher.

A scientist has index h if h of their N papers have at least h citations each, and the other N - h papers have no more than h citations each. If there are multiple possible values for h, the maximum value is used.

Given an array of natural numbers, with each value representing the number of citations of a researcher's paper, return the h-index of that researcher.

For example, if the array was:

[4, 1, 0, 2, 3]
This means the researcher has 5 papers with 4, 1, 0, 2, and 3 citations respectively. The h-index for this researcher is 2, since they have 2 papers with at least 2 citations
'''

input_arr = [4,1,0,2,3]

def naive_solution(input_arr):
    '''
    While counts >= index, keep iterating to check for index values
    index: [0,1,2,3,4,5,6]
    input: [0,0,0,7,7,7,7]
    For each iteration, check that there are at least i papers with i citations

    Since len(input) == 7, start checking from 7
        - 7: len([x for x in input if x >= 7]) == 4
        - 6: len([x for x in input if x >= 6]) == 4
        - 5: len([x for x in input if x >= 4]) == 4
        - 4: len([x for x in input if x >= 4]) == 4

    In the worst case, we iterate through all $n$ items in the aray if all of them are 0

    Time complexity: O(N^2). We incur O(N) for the outer loop (to check every value of `h`) and O(N) for the inner loop (to check if each value is >= `i`)
    Space complexity: O(1)
    '''
    for i in range(len(input_arr),-1,-1):
        check_len = len([x for x in input_arr if x >= i])
        if check_len >= i:
            return i
    return 0

def sort_and_loop(input_arr):
    '''
    Instead of looping twice, we can sort the input, then loop only once! The idea being, once we have a sorted input, we don't need to loop over every value in the array. 

    Time complexity: O(n log n). We sort in O(n log n), and loop in O(n), so overall complexity is n log n
    Space complexity: O(n)
    '''
    sorted_input = sorted(input_arr, key=lambda x: -x)
    for h in range(len(sorted_input)):
        if sorted_input[h] >= h+1:
            continue
        else:
            return h

def binary_search(input_arr):
    '''
    Another way to think about it is to do binary search. The idea is that, with an ordered array, either your midpoint meets the h-index criteria, or it does not meet the criteria.
        - There can only be 1 possible h-index for any given array
        - If a h-index x is valid, it must also supercede values x-1, x-2 etc
        - If a h-index x is NOT valid, it must also not be valid for x+1, x+2 etc
        - So we can recursively half the search space until we reach the point where we can neither increase nor decrease x!
    - We perform binary search log(n) times 
    - In each interation, we scan the entire array to see if value is valid at O(N) cost
    - This gives us O(n log n)

    Time complexity: O(n log n) 
    Space complexity: O(1)
    '''
    sorted_arr = sorted(input_arr, key=lambda x: -x)
    left = 0
    right = len(sorted_arr) ##4
    hindex = 0

    while right >= left:
        mid = (left+right)//2 
        # print(f"{left=}, {right=}, {mid=}")
        if sorted_arr[mid] >= (mid+1):
            ## If, at the midpoint, the value exceeds or equals the index, it must be true that there are at least `mid` number of citations that are >= mid
            ## We continue the loop to check if the values to the right of the midpoint increases the h-index
            hindex = mid+1
            left = mid+1
        elif sorted_arr[mid] < (mid+1):
            ## If, at the midpoint, the value is less than the index, it must be true that there are fewer than `mid` number of citations that are >= mid
            ## No point in checking right hand side of array, because the involves increasing the h-index, and we already know that the midpoint does not exceed h!
            right = mid-1

    return hindex

