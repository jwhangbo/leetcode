# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # pre-order traversal can be used to calculate the good nodes via DFS algorithm
        # both the time complexity and memory complexity will be O(n)

        # create the recursive DFS function - note that an additional parameter will be used to pass the maximum node value
        def dfs(node, max_val):
            
            # create a base case for the recursive function by checking if the node is null
            # if a node is null, the number of good nodes would be 0
            if not node:
                return 0
            
            # check if the current node's value is greater than or equal to max_val and return 1 if true, else 0
            res = 1 if node.val >= max_val else 0

            # find the new max_val by calculating the maximum between max_val and the current node's value
            max_val = max(max_val, node.val)

            # check if the left and right children nodes are good nodes recursively
            # ensure that res is used to sum the number of good nodes found via DFS
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)

            # return the total sum
            return res

        # if code reaches this point, the recursive DFS function will have found all good nodes in the binary tree
        return dfs(root, root.val)