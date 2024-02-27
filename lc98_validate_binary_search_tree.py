# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # primitive approach is to brute force check every value in a node's left and right subtrees
        # this would be O(n^2) time complexity
        
        # instead, DFS algorithm can be used to optimize the time complexity to O(n)

        # create the recursive DFS function - note that two additional parameters will be needed for the left and right children nodes
        def dfs(node, left, right):

            # create a base case for the recursive function by checking if the node is null
            # if a node is null, it would be a valid binary search tree
            if not node:
                return True
            
            # check if the current node's value is less than left or greater than right
            # if true, the tree would not be a valid binary search tree
            if not(node.val < right and node.val > left):
                return False
            
            # recursively run the DFS function on the left and right children nodes
            # for the left child node, the right parameter would be updated to use the current node value instead
            # this is due to the fact that the previous statement validated that the current node is less than right
            # therefore, it should be updated to use the 'lesser' value of the two
            # likewise, the right child node would have the left parameter updated to use the current node value
            return (dfs(node.left, left, node.val) and dfs(node.right, node.val, right))
        
        # run the DFS function on the root node
        # set the left and right parameters as negative and positive infinity as placeholder values
        return dfs(root, float("-inf"), float("inf"))