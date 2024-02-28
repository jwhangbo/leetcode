# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursive approch can be used to generate a sorted list in order to find the Kth smallest element
        # however, an iterative approach can be used instead

        # initialize a counter in order to calculate when the Kth smallest element is found
        n = 0

        # initialize a stack
        stack = []

        # initialize a pointer that defaults to the root node
        curr = root

        # loop while the stack is not empty and while the curr pointer is not null
        while stack or curr:

            # loop until the leftmost node has been found
            while curr:

                # insert the current node to the stack before moving down the BST to its left child node
                # at this point in the approach, the value of the node itself is not utilized
                stack.append(curr)
                curr = curr.left

            # once the leftmost node has been found, pop from the stack
            # a BST at its leftmost node would contain the lowest value, which can be checked against the given k parameter
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val

            # since the leftmost node did not match, check its right child node on the next loop cycle
            # note that a final return statement is not needed due to the guarantee that there are k nodes in the BST
            curr = curr.right