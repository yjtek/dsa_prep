Leetcode Link: https://leetcode.com/problems/valid-anagram/solutions/3248051/242-valid-anagram/

## 242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

### Examples 

Example 1:
    - Input: s = "anagram", t = "nagaram"
    - Output: true

Example 2:
    - Input: s = "rat", t = "car"
    - Output: false

### Constraints:

- $1 <= \text{s.length, t.length} <= 5 * 10^4$
- `s` and `t` consist of lowercase English letters.

### Follow up 

- What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

- Can you solve this in O(1) memory

### Starter Code
```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ...
```