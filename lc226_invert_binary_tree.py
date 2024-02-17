# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # depth-first search (DFS) algorithm can be used for this approach
        # since the child nodes must also be inverted with its parent node, recursion is preferred

        # create a base case for the recursive function by checking if the root is null 
        if not root:
            return None
        
        # if not, swap the children nodes
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # continue inversing the children nodes by calling on the recursive function
        self.invertTree(root.left)
        self.invertTree(root.right)

        # if code reaches this point, the recursive function will have completed and all nodes will have been inversed
        return root