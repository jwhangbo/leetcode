# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # brute force approach would be to check every node and check if its subtrees are balanced, with time complexity at O(n^2)
        # alternatively, recursive DFS can be used to reduce time complexity to O(n)

        # create the recursive DFS function
        def dfs(root):

            # create a base case for the recursive function by checking if the node is null
            # the DFS function will return two values, one for checking if the subtrees are balanced and the other for the current height
            if not root:

                # since this is the base case, the subtrees will be balanced and the height should be 0
                return [True, 0]
            
            # find the height of the left and right subtree recursively
            left, right = dfs(root.left), dfs(root.right)

            # check if the subtrees are balanced by taking the absolute value of the two heights and seeing if it is equal or less than 1
            # moreover, the boolean to check if the subtrees are balanced should also be checked
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            # return the first value, the boolean for subtrees being balanced
            # the second value will be the current height, calculated by 1 + the maximum between the left and right subtrees
            return [balanced, 1 + max(left[1], right[1])]

        # if code reaches this point, the recursive DFS function will have checked if the given binary tree is balanced or not
        return dfs(root)[0]