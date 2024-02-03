'''
Given a list of integers L, find the maximum length of a sequence of consecutive numbers that can be formed using elements from L.

For example, given L = [5, 2, 99, 3, 4, 1, 100], return 5 as we can build a sequence [1, 2, 3, 4, 5] which has length 5.
'''

def my_answer(input_arr):
    '''
    1. O(n log n) time: Sort input 
    2. O(n) time, O(n) space: Store an array diffs showing the difference between 2 consecutive values. 
    3. O(1) time: Split by 0, cumsum, take max+1
    4. This is the largest number of consecutive elements in the array
    '''
    sorted_arr = sorted(input_arr)
    diffs = [sorted_arr[i+1] - sorted_arr[i] for i in range(len(sorted_arr)-1)]
    diffs = ['1' if x == 1 else '0' for x in diffs]
    lengths = ''.join(diffs).split('0')
    maxlen = max([len(x) for x in lengths]) + 1
    return maxlen

def my_answer_2(input_arr):
    '''
    1. Instead of trying to sort, as per previous answer, we can actually do this in O(N)
    2. O(N) time: First, convert input array into hashset
    3. O(N) time: Then, loop over every element in the input_arr
        - O(1) Check if number - 1 is in the hashset 
        - If it is, then we don't have to check the length of the consecutive string starting from this value 
        - O(N) time: If it isn't, this is a start of a substring, and so we iteratively look for number + 1 in the hashset. This is O(N) in the worst case

    '''
    input_set = set(input_arr)
    maxlen = 0

    for element in input_set:
        if element-1 in input_set:
            continue
        
        input_len = 1
        while element + 1 in input_set:
            input_len += 1
            element += 1
        maxlen = max(maxlen, input_len)
    
    return maxlen
    