# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')
POLYNOMIAL=int(10)
PRIME1=int(1e9+7)

# def solve(s, t):
# 	ans = Answer(0, 0, 0)
# 	for i in range(len(s)):
# 		for j in range(len(t)):
# 			for l in range(min(len(s) - i, len(t) - j) + 1):
# 				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
# 					ans = Answer(i, j, l)
# 	return ans

def naive_solve(s,t):
	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans

def precompute_cumulative_hash(string, prime):
    '''
    See Q4 for computation. Basically we use the relation that for string `s`, the hash `H()` of s[2:4] is simply H(s[0:4]) - H(s[0:2]) * x^2
    '''
    hashvals_arr = [int(0)] * (len(string)+1)
    for i in range(len(string)):
        hashvals_arr[i+1] = int(
            (((hashvals_arr[i] * POLYNOMIAL) % prime) + ord(string[i]))
            % prime
        )
    return hashvals_arr

def get_hashmap_for_substrings(string, string_cumulative_hash, substring_len, prime):
    '''
    Returns a map with the hashvalues as keys, and substring starting indices as values.

    Note that the formula provided in the course is not accurate. Because there is a subtraction term, it is possible that you can end up with a negative number. As such, always add `prime` to the final sum to ensure that you are dealing with positive values. Adding `prime` doesn't change the final modulo, because prime % prime = 0, and won't affect the final answer by modular arithmetic.
    '''
    # substr_hashes = [0.] * (len(string)-substring_len+1)
    substr_hash_map = {}
    polynomial_term = pow(int(POLYNOMIAL), int(substring_len), int(prime))

    for substring_start_index in range(len(string)-substring_len+1):
        substring_end_index = substring_start_index+substring_len
        hashval = int((
            ##add `prime` to avoid negative values!!
            prime +
            string_cumulative_hash[substring_end_index] - 
            ((string_cumulative_hash[substring_start_index] * polynomial_term) % prime)
        ) % prime)
        # print(f'{substring_start_index}, {substring_end_index}, {string[substring_start_index:substring_end_index]}, {hashval}')
        if hashval in substr_hash_map:
            substr_hash_map[hashval].append(substring_start_index) 
        else:
            substr_hash_map[hashval] = [substring_start_index]
    return substr_hash_map

def get_common_substring_index(string, string_cumulative_hash, string_to_compare, hash_to_compare, substring_len, prime):
    # substr_hashes = [0.] * (len(string)-substring_len+1)
    polynomial_term = pow(int(POLYNOMIAL), int(substring_len), int(prime))

    for substring_start_index in range(len(string)-substring_len+1):
        substring_end_index = substring_start_index+substring_len
        hashval = (
            string_cumulative_hash[substring_end_index] - 
            ((string_cumulative_hash[substring_start_index] * polynomial_term) % prime) + 
            prime
        ) % prime
        if hashval in hash_to_compare:
            for index in hash_to_compare.get(hashval):
                if string[substring_start_index:(substring_start_index+substring_len)] == string_to_compare[index:(index+substring_len)]:
                    return index, substring_start_index
    return -1, -1

def solve(s, t):
    
    max_common_substr_len = min(len(s), len(t))
    min_common_substr_len = 0
    max_matching_substring_len = 0
    string1_match_index, string2_match_index = -1, -1
    
    s_hashval_arr_p1 = precompute_cumulative_hash(s, PRIME1)
    t_hashval_arr_p1 = precompute_cumulative_hash(t, PRIME1)
    # s_hashval_arr_p2 = precompute_cumulative_hash(s, PRIME2)
    # t_hashval_arr_p2 = precompute_cumulative_hash(t, PRIME2)

    while max_common_substr_len >= min_common_substr_len:
        # print('='*50)
        check_length: int = (min_common_substr_len + max_common_substr_len)//2
        # print(f"{max_common_substr_len=}, {min_common_substr_len=}, {check_length=}")

        s_substring_hash_p1 = get_hashmap_for_substrings(s, s_hashval_arr_p1, check_length, PRIME1)
        
        ## For debugging
        t_substring_hash_p1 = get_hashmap_for_substrings(t, t_hashval_arr_p1, check_length, PRIME1)
        
        has_common_substring_p1 = False
        common_substring_string1_index_p1, common_substring_string2_index_p1  = get_common_substring_index(string=t, string_cumulative_hash=t_hashval_arr_p1, string_to_compare=s, hash_to_compare=s_substring_hash_p1, substring_len=check_length, prime=PRIME1)
        
        # print(common_substring_string1_index_p1, common_substring_string2_index_p1)
        common_hash_found = common_substring_string1_index_p1 != -1
        is_not_collision = s[common_substring_string1_index_p1:(common_substring_string1_index_p1+check_length)] == t[common_substring_string2_index_p1:(common_substring_string2_index_p1+check_length)]
        # print(f'{common_hash_found=}, {is_not_collision=}')
        if common_hash_found and is_not_collision:
            has_common_substring_p1 = True
        
        if has_common_substring_p1:
            # print(s[common_substring_string1_index_p1:(common_substring_string1_index_p1+check_length)], t[common_substring_string2_index_p1:(common_substring_string2_index_p1+check_length)])
            max_matching_substring_len = check_length
            min_common_substr_len = check_length+1
            string1_match_index = common_substring_string1_index_p1
            string2_match_index = common_substring_string2_index_p1
        else:
            max_common_substr_len = check_length-1
        # print(f"{max_common_substr_len=}, {min_common_substr_len=}")

    return Answer(string1_match_index, string2_match_index, max_matching_substring_len)

for line in sys.stdin.readlines():
	s, t = line.split()
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)
