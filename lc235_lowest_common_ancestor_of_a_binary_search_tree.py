# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # the LCA can be found by checking every 'split' between the nodes
        # therefore, the time complexity is O(logn), as only one node can be visited per level in the tree
        # likewise, the memory complexity is O(1) as no data structure is required

        # initialize the current node as the root
        cur = root
        
        # loop until the node is null
        while cur:

            # check if both the p and q values are greater than the current value
            if p.val > cur.val and q.val > cur.val:

                # go down the right subtree by changing the current node to the right child node
                cur = cur.right
            
            # check if both the p and q values are less than the current value
            if p.val < cur.val and q.val < cur.val:
                
                # go down the left subtree by changing the current node to the left child node
                cur = cur.left
            
            # else, the 'split' has been found
            else:
                return cur