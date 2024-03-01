# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # brute force approach is to check every node and sum its left and right subtrees
        # DFS algorithm can be used to optimize the approach to O(n) time complexity and O(h) memory complexity
        # the key is to take the maximum of the two available children node options and pass it up to the parent node

        # initialize a list to store the result, the max sum found so far by the recursive DFS function
        # set the root value as the default
        res = [root.val]
        
        # create the recursive DFS function, using the root node as the parameter
        def dfs(root):
            
            # create a base case for the recursive function by checking if the root is null
            if not root:
                return 0
            
            # recursively run the DFS function on the left and right children node
            # track the return value by saving them to the local left_max or right_max
            # these local max values would find the maximum path value at each respective level of the binary tree
            left_max = dfs(root.left)
            right_max = dfs(root.right)

            # check if the left_max or right_max values are negative
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # check for the case of finding the max path sum with a split, which is when both the children nodes are used
            res[0] = max(res[0], root.val + left_max + right_max)

            # check for the case of finding the max path sum without a split, which is when either the left or right node is used
            # this will be returned in order to pass 'up' the local maximum to the parent node
            # note that to avoid having to use a global variable to store the max path sum, an adjustment can be made
            # the DFS function can instead return both cases within a single return statement and use the greater of the two at the end
            return root.val + max(left_max, right_max)
        
        # run the DFS function on the root node
        dfs(root)

        # if the code reaches this point, the DFS function would have found the max path sum of the given binary tree
        return res[0]