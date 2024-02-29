# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder traversal is to start at the root as the current node and then move down to the left and right subtrees
        # inorder traversal is go from the leftmost node to the rightmost node

        # the approach will use the fact that preorder traversal will always have the root node as its first node
        # moreover, the inorder traversal can be used to parition the preorder traversal to find where the left and right subtrees are

        # set the base case to check if there are no nodes to traverse, and return null if true
        if not preorder or not inorder:
            return None
        
        # initialize a TreeNode with the root set to the first value of the preorder traversal
        root = TreeNode(preorder[0])
        
        # find the index to partition the preorder traversal by finding where the root index is in the inorder traversal
        mid = inorder.index(preorder[0])

        # recursively build the left and right subtrees by partitioning the preorder and inorder traversals
        # for the left subtree, the new preorder traversal should be all of the nodes after the root node until the partition index
        # likewise, the inorder traversal should be all of the nodes until the parition index
        # note that for the inorder traversal, the 'mid' node is not included in the partition, as mid is the root index
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        # for the right subtree, the new preorder traversal should be all of the nodes after the partition index
        # likewise, the inorder traversal should be all of the nodes after the parition index
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        # if code reaches this point, the preorder and inorder traversals would have finished constructing the binary tree
        return root