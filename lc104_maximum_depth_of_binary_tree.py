# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # three possible approaches - one will be recursive while the two others will be iterative
        # first approach is to use recursive DFS
        # both time and memory complexity will be O(n)

        # check if root exists and return 0 if not
        if not root:
            return 0
        
        # recursively return the children nodes, which will increment for each depth
        # taking the max of the children nodes will ensure that the greater depth between the two will be returned
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    

        # if recursion is not allowed, iterative breadth-first search (BFS) can be used instead
        # a queue can be used to store nodes; for each increment between parent and children nodes, the depth will also be incremented
        # once the queue is empty, the maximum depth will have been found
    
        # check if root exists and return 0 if not
        # if not root:
        #     return 0
    
        # initialize the level to represent the current depth and a queue
        # level = 0
        # q = deque([root])
    
        # loop until the queue is empty
        # while q:
    
            # check each node in the queue and pop it, then add its children nodes to the queue
            # for i in range(len(q)):
                # node = q.popleft()
                # if node.left:
                    # q.append(node.left)
    
                # if node.right:
                    # q.append(node.right)
        
            # increment the level after each queue state
            # level += 1
        
        # if code reaches this point, the level will represent the maximum depth
        # return level
    

        # finally, similar to iterative BFS, iterative DFS can be used instead of recursive
        # for this approach, a stack is used to store both the node and its depth
    
        # initialize a stack with root at depth 1 and the result to store the maximum depth
        # stack = [[root, 1]]
        # res = 1
    
        # loop until the stack is empty
        # while stack:
    
            # pop the node and its depth
            # node, depth = stack.pop()
    
            # check if node is not null, and add its children nodes if true
            # if node:
                # res = max(res, depth)
                # stack.append([node.left, depth + 1])
                # stack.append([node.right, depth + 1])
    
        # if code reaches this point, the res will represent the maximum depth
        # return res