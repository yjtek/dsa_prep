def longest_palindromic_substring_dp(s: str) -> str:
    ## Start from length 1 strings, build up to length N strings
    dp = [[False]*len(s) for x in range(len(s))]
    longest_palindrome = s[0]
    for string_len in range(1, len(s)+1):
        for string_start_index in range(len(s)-string_len+1):
            if string_len == 1:
                dp[string_start_index][string_start_index]=True
            elif (string_len == 2) & (s[string_start_index] == s[string_start_index+string_len-1]):
                dp[string_start_index][string_start_index+string_len-1] = True
                if len(longest_palindrome) < string_len:
                    longest_palindrome = s[string_start_index:(string_start_index+string_len)]
            elif (string_len > 2) & (s[string_start_index] == s[string_start_index+string_len-1]) & (dp[string_start_index+1][string_start_index+string_len-2]):
                dp[string_start_index][string_start_index+string_len-1] = True
                if len(longest_palindrome) < string_len:
                    longest_palindrome = s[string_start_index:(string_start_index+string_len)]
    return longest_palindrome

if __name__ == '__main__':
    lps = longest_palindromic_substring_dp('abba')
    