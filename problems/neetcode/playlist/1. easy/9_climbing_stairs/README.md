Leetcode Link: https://leetcode.com/problems/climbing-stairs/description/

## 70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note, here "top" refers to the step AFTER the n-th step. So if you're on the n-th step, you can take 1 step to reach the top, giving you 1 way to reach the top

### Examples 

Example 1:
- Input: n = 2
- Output: 2
- Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
- Input: n = 3
- Output: 3
- Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

### Constraints:
- 1 <= n <= 45

### Starter Code
```
class Solution:
    def climbStairs(self, n: int) -> int:
        ...
```