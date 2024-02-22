# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # logic will be similar to problem 100 but with an additional recursive function to check each node
        
        # if the subRoot is null, it would be a valid subtree of the root
        if not subRoot:
            return True
        
        # conversely, if the root is null, then the subRoot will never be a valid subtree of the root
        if not root:
            return False
        
        # on the current root node, check if the subRoot is a valid subtree of the root
        if self.sameTree(root, subRoot):
            return True
        
        # since the current node is not a valid subtree, traverse down each node recursively for both of their respective children nodes
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    # the sameTree function will be very similar logic to problem 100
    def sameTree(self, root, subRoot):
        
        # check if both the root and and subRoot are null
        if not root and not subRoot:
            return True
        
        # check if both root and subRoot exist and that the root node values are equal
        if root and subRoot and root.val == subRoot.val:

            # if true, continue traversing down the root's children nodes and confirm if the subRoot is a valid subtree
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        
        # else, the subRoot cannot be a valid subtree
        return False