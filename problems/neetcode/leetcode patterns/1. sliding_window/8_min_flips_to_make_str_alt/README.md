Leetcode Link: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/

## 1888. Minimum Number of Flips to Make the Binary String Alternating

You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

### Examples 

- Example 1:
    - Input: s = "111000"
    - Output: 2
    - Explanation: Use the first operation two times to make s = "100011". Then, use the second operation on the third and sixth elements to make s = "101010".

- Example 2:
    - Input: s = "010"
    - Output: 0
    - Explanation: The string is already alternating.

- Example 3:
    - Input: s = "1110"
    - Output: 1
    - Explanation: Use the second operation on the second element to make s = "1010".
 
### Constraints:

- `1 <= s.length <= 10^5`
- s[i] is either '0' or '1'

### Starter Code
```
class Solution:
    def minFlips(self, s: str) -> int:
        ...
```

01001001101
01010101010
00011100111 --> 6

01001001101
10101010101
11100011000 --> 5

+++

10010011010
01010101010
11000110000 --> 4

10010011010
10101010101
00111001111 --> 7

+++

00100110101
01010101010
01110011111 --> 8

00100110101
10101010101
10001100000 --> 3

+++

01001101010
01010101010
00011000000 --> 2

01001101010
10101010101
11100111111 --> 9

+++

10011010100
01010101010
00011000000 --> 2

10011010100
10101010101
11100111111 --> 9