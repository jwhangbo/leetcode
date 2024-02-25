# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # very similar approach to problem 102, but with an additional step of taking the rightmost value at each level
        # since BFS algorithm is used, time and memory complexity will be O(n)

        # initialize a list of results to store the values of each node and its respective level
        res = []

        # initialize a queue and default to the root node
        q = collections.deque([root])

        # loop until the queue is empty
        while q:

            # initialize a placeholder node to track the rightmost value, defaulting to null
            right_side = None

            # save the length of the current queue
            q_len = len(q)

            # check each node in the queue and check if it's not null
            for i in range(q_len):
                node = q.popleft()
                if node:

                    # set the rightmost node as the current node
                    right_side = node

                    # insert its children nodes afterwards, left must be inserted first to maintain order
                    q.append(node.left)
                    q.append(node.right)

            # if right_side is not null, append the node's value to the results list
            if right_side:
                res.append(right_side.val)
        
        # if code reaches this point, res will contain the value of nodes seen from the right side of the binary tree
        return res