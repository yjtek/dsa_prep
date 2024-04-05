# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')
POLYNOMIAL=10
PRIME1=1e9+7

# def solve(s, t):
# 	ans = Answer(0, 0, 0)
# 	for i in range(len(s)):
# 		for j in range(len(t)):
# 			for l in range(min(len(s) - i, len(t) - j) + 1):
# 				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
# 					ans = Answer(i, j, l)
# 	return ans

def precompute_cumulative_hash(string, prime):
    '''
    See Q4 for computation. Basically we use the relation that for string `s`, the hash `H()` of s[2:4] is simply H(s[0:4]) - H(s[0:2]) * x^2
    '''
    hashvals_arr = [0.] * (len(string)+1)
    for i in range(len(string)):
        hashvals_arr[i+1] = (((hashvals_arr[i] * POLYNOMIAL) % prime) + ord(string[i])) % prime
    return hashvals_arr

def compute_substring_hashvals(string, string_cumulative_hash_arr, substring_len, prime):
    # substr_hashes = [0.] * (len(string)-substring_len+1)
    substr_hash_map = {}
    polynomial_term = 1
    for _ in range(substring_len):
        polynomial_term = (polynomial_term * POLYNOMIAL) % prime

    for substring_start_index in range(len(string)-substring_len+1):
        substring_end_index = substring_start_index+substring_len
        hashval = (
            string_cumulative_hash_arr[substring_end_index] - 
            (string_cumulative_hash_arr[substring_start_index] * polynomial_term)
        ) % prime
        if hashval in substr_hash_map:
            substr_hash_map[hashval].append(substring_start_index) 
        else:
            substr_hash_map[hashval] = [substring_start_index]
    return substr_hash_map

def get_common_substring_index(string, string_cumulative_hash_arr, hash_to_compare, substring_len, prime):
    # substr_hashes = [0.] * (len(string)-substring_len+1)
    substr_hash_map = {}
    polynomial_term = 1
    for _ in range(substring_len):
        polynomial_term = (polynomial_term * POLYNOMIAL) % prime

    for substring_start_index in range(len(string)-substring_len+1):
        substring_end_index = substring_start_index+substring_len
        hashval = (
            string_cumulative_hash_arr[substring_end_index] - 
            (string_cumulative_hash_arr[substring_start_index] * polynomial_term)
        ) % prime
        if hashval in hash_to_compare:
            return hash_to_compare.get(hashval)[0], substring_start_index
    return -1, -1

def solve(s, t):
    
    max_common_substr_len = min(len(s), len(t))
    min_common_substr_len = 0
    max_matching_substring_len = 0
    string1_match_index = 0
    string2_match_index = 0

    while max_common_substr_len >= min_common_substr_len:
        # print('='*50)
        # print(f"{max_common_substr_len=}, {min_common_substr_len=}")
        check_length = (min_common_substr_len + max_common_substr_len)//2
        s_hashval_arr_p1 = precompute_cumulative_hash(s, PRIME1)
        t_hashval_arr_p1 = precompute_cumulative_hash(t, PRIME1)

        s_substring_hash_p1 = compute_substring_hashvals(s, s_hashval_arr_p1, check_length, PRIME1)
        common_substring_string1_index, common_substring_string2_index  = get_common_substring_index(t, t_hashval_arr_p1, s_substring_hash_p1, check_length, PRIME1)
        has_common_substring = common_substring_string1_index != -1
        # print(s[common_substring_string1_index:(common_substring_string1_index+check_length)], t[common_substring_string2_index:(common_substring_string2_index+check_length)])

        if has_common_substring:
            max_matching_substring_len = check_length
            min_common_substr_len = check_length+1
            string1_match_index = common_substring_string1_index
            string2_match_index = common_substring_string2_index
        else:
            max_common_substr_len = check_length-1
        # print(f"{max_common_substr_len=}, {min_common_substr_len=}")

    return Answer(string1_match_index, string2_match_index, max_matching_substring_len)

for line in sys.stdin.readlines():
	s, t = line.split()
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)
