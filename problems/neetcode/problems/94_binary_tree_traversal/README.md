Leetcode Link: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

## 94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

### Examples 

Example 1:
- Input: root = [1,null,2,3]
- Output: [1,3,2]

Example 2:
- Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
- Output: [4,2,6,5,7,1,3,9,8]

Example 3:
- Input: root = []
- Output: []

Example 4: 
- Input: root = [1]
- Output: [1]

### Constraints:

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

### Follow up 
- Recursive solution is trivial, could you do it iteratively?

### Starter Code
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ...
```