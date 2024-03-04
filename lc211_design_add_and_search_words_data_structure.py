# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    # create a TrieNode object to track the children nodes and if the node is the end of the word

    def __init__(self):

        # initialize a hashmap for the children and a bool to track if the node is the end of the word
        self.children = {}
        self.end_of_word = False

class WordDictionary:
    # similar to problem 208

    def __init__(self):
        # initialize a TrieNode for the root node
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        
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
        
        # create the recursive DFS function, using the current index and root node as parameters
        def dfs(j, root):

            # initialize cur to point to the root node
            cur = root

            # iterate each character in the word to check if it exists in the trie
            for i in range(j, len(word)):
                c = word[i]

                # since the dot acts as a wildcard, check against every child in the children hasmhap
                if c == ".":
                    for child in cur.children.values():
                        
                        # run the DFS function with the index incremented, as the dot is effectively ignored
                        if dfs(i + 1, child):
                            return True
                    
                    # otherwise, return false
                    return False

                else:
                    
                    # check if c is not in the children hashmap for the current node, and return false if true
                    if c not in cur.children:
                        return False
                    
                    # move pointer to point to the child node
                    cur = cur.children[c]
            
            # return the last node's end_of_word
            return cur.end_of_word
        
        # run the DFS function on the first index and root node and return the result
        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)