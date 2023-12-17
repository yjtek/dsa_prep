'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

## MY SOLUTION
def reverse(self, x: int) -> int:        
    holder = int(str(abs(x))[::-1])
    
    if holder.bit_length() >= 32:
        return 0
    else:
        if x < 0:
            return 0 - holder
        else:
            return holder

## Least memory solution
class Solution(object):
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        return (-rev if x < 0 else rev) if rev.bit_length() < 32 else 0

## Succinct way of getting sign
class Solution:
    def reverse(self, x):
        sign = [1,-1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0

## Fastest solution
class Solution:
    def reverse(self, x: 'int') -> 'int':
        sign = 1
        if x < 0:
            sign = -1
        num = 0
        x = abs(x)
        while x > 0:
            d = x % 10 
            x = x // 10
            num = num*10 + d
        if (num> (2**31) -1):
            return 0
        return num * sign
