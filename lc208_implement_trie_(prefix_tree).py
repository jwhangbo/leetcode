# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    # create a TrieNode object to track the children nodes and if the node is the end of the word

    def __init__(self):

        # initialize a hashmap for the children and a bool to track if the node is the end of the word
        self.children = {}
        self.end_of_word = False

class Trie:
    # prefix trees are very efficient at checking for prefix strings, with time complexity at O(1)

    def __init__(self):

        # initialize a TrieNode for the root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        # initialize cur to point to the root node
        cur = self.root

        # iterate each character in the word to insert nodes to the trie
        for c in word:

            # check if c is not already in children, and create a new TrieNode if true
            if c not in cur.children:
                cur.children[c] = TrieNode()

            # move pointer to point to the child node
            # note that the above check ensures that children will always contain c
            cur = cur.children[c]
        
        # set the last node's end_of_word to true once the word has been fully iterated
        cur.end_of_word = True
        

    def search(self, word: str) -> bool:

        # initialize cur to point to the root node
        cur = self.root

        # iterate each character in the word to check if it exists in the trie
        for c in word:

            # check if c is not in the children hashmap for the current node, and return false if true
            if c not in cur.children:
                return False

            # move pointer to point to the child node
            cur = cur.children[c]
        
        # return the end_of_word bool to check if the final node is the last character of the word
        return cur.end_of_word


    def startsWith(self, prefix: str) -> bool:
        
        # initialize cur to point to the root node
        cur = self.root

        # iterate each character in the prefix to check if it exists in the trie
        for c in prefix:
            
            # check if c is not in the children hashmap for the current node, and return false if true
            if c not in cur.children:
                return False
            
            # move pointer to point to the child node
            cur = cur.children[c]

        # if code reaches this point, the prefix must be in the trie
        return True

    

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)