# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # optimal approach is to use the BFS algorithm to traverse by level and saving the values of each level in a queue
        # both the time and memory complexity will be O(n) since each node will only be visited once
        # technically, the memory complexity would be O(n/2) as the queue can hold at most half of n, but this gets rounded up

        # initialize a list of results to store the values of each node and its respective level
        res = []

        # initialize a queue and insert the root node
        q = collections.deque()
        q.append(root)

        # loop until the queue is empty
        while q:

            # save the length of the current queue
            q_len = len(q)

            # initialize a list to store the current level's node values
            level = []

            # check each node in the queue and insert its children nodes afterwards
            for i in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            # if the level list is not empty, append to the results list
            if level:
                res.append(level)
        
        # if code reaches this point, res will contain the level order traversal of its nodes' values
        return res