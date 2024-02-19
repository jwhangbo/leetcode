# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # brute force approach would be to check every node and calculate its diameter, with time complexity at O(n^2)
        # alternatively, recursive DFS can be used to reduce time complexity to O(n)

        # initialize a result variable
        res = [0]

        # create the recursive DFS function
        def dfs(root):

            # create a base case for the recursive function by checking if the node is null
            # return -1 instead of 0 to be consistent with the logic of the approach
            if not root:
                return -1
            
            # find the height of the left and right subtree recursively
            left = dfs(root.left)
            right = dfs(root.right)

            # check the new height (left + right + 2) against the existing maximum diameter
            res[0] = max(res[0], left + right + 2)

            # return 1 + the maximum height between the left and right subtrees
            return 1 + max(left, right)
        
        # run the recursive function on the root node
        dfs(root)

        # if code reaches this point, the diameter of the binary tree will have been found
        return res[0]