'''
Given a sorted array arr of distinct integers, return the lowest index i for which arr[i] == i. Return null if there is no such index.

For example, given the array [-5, -3, 2, 3], return 2 since arr[2] == 2. Even though arr[3] == 3, we return 2 since it's the lowest index.
'''

def naive_ans(sorted_int_array) -> int:
    '''
    Loop over the array, and return if condition array[i] = 2 is met

    Time complexity: O(N)
    Space complexity: O(1)
    '''
    for i in range(len(sorted_int_array)):
        if sorted_int_array[i] == i:
            return i
    return None

def find_index_eq_val(input_arr):
    '''
    Let's suppose we have an array [1,3,5,7,9]
    Positions as [0,1,2,3,4]
    We start at position 2, and find that array[2] = 5 > 2
    So we need a smaller position, and smaller position value. 
    We search left half of array
    In total, we search a maximum of floor(log_2(2)) times
    Time complexity: O(log N)
    '''
    len_input = int(np.floor(math.log2(len(input_arr))))
    max_tries = len_input + 1
    mid = len_input//2
    for i in range(max_tries):
        if input_arr[mid] == mid:
            return mid
        elif input_arr[mid] > mid:
            mid = len(input_arr[(mid+1):])//2
        elif input_arr[mid] < mid:
            mid = len(input_arr[:mid])//2
    return None    
    
        
if __name__ == '__main__':
    print(find_index_eq_val([-5, -3, 2, 3]))
    

