Leetcode Link: https://leetcode.com/problems/squares-of-a-sorted-array/description/

## 977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

### Examples 

Example 1:
- Input: nums = [-4,-1,0,3,10]
- Output: [0,1,9,16,100]
- Explanation: After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100].

Example 2:
- Input: nums = [-7,-3,2,3,11]
- Output: [4,9,9,49,121]

### Constraints:
- $1 <= nums.length <= 10^4$
- $10^4 <= nums[i] <= 10^4$
- nums is sorted in non-decreasing order
 
### Follow up 
- Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?


### Starter Code
```
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ...
```