# 100. Same Tree
# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive DFS can be used for this approach

        # check if both the p and q nodes are null
        if not p and not q:
            return True
        
        # check if either the p or q nodes are null or if the values do not match
        if not p or not q or p.val != q.val:
            return False
        
        # traverse down each node recursively for both of their respective children nodes
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))