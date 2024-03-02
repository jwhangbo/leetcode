# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # preorder traversal via DFS algorithm can be used for the approach, with a time complexity of O(n)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        # initialize an empty list to store all nodes as strings
        res = []

        # create the recursive DFS function, using a node as the parameter
        def dfs(node):

            # create a base case for the recursive function by checking if the node is null
            # if null, append N to res to track that it's a null node
            if not node:
                res.append("N")
                return

            # append the current node's value to res as a string
            res.append(str(node.val))

            # recursively traverse down the left and right subtrees
            dfs(node.left)
            dfs(node.right)
            
        # run the DFS function on the root node
        dfs(root)

        # if the code reaches this point, the DFS function would have added all nodes to the list
        # convert the list to a comma delimited string before returning
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        # since the serialized output will be a comma delimited string, split the string into a list
        vals = data.split(",")

        # initialize a pointer to track the index for vals
        self.i = 0

        # create the recursive DFS function
        def dfs():

            # check if the pointer's value is a null node
            if vals[self.i] == "N":

                # increment i and return None
                self.i += 1
                return None
            
            # initialize a TreeNode with the root value as the current node's value
            node = TreeNode(int(vals[self.i]))

            # increment i
            self.i += 1
            
            # recursively traverse down the left and right subtrees
            # since preorder traversal was used to serialize, the left subtree will always be first
            # likewise, by the time the recursive DFS function finishes, i will be pointing to the first value of the right subtree
            node.left = dfs()
            node.right = dfs()

            # if the code reaches this point, the DFS function would have finished deserializing the encoded data into a tree
            return node

        # run the recursive DFS function and return the output afterwards
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))