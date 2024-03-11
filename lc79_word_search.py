# 79. Word Search
# https://leetcode.com/problems/word-search/

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # this problem must be brute forced in order to solve, but backtracking can be used
        # the time complexity will be O(row * col * 4^n), where n is the length of the word
        # the 4 in 4^n comes from running the recursive DFS function at all four possible adjacent cells

        # initialize constants to store the length of the rows and columns of the board
        ROWS, COLS = len(board), len(board[0])

        # initialize a set to store the path in order to prevent reusing the previous cell in the recursive DFS function
        path = set()

        # create the recursive DFS function, using the current row, column and index as parameters
        def dfs(r, c, i):

            # create a base case for the recursive function by checking if i equals the length of word
            if i == len(word):
                return True
            
            # check all possible cases where the DFS function would have to return False
            # these include i being out of bounds, the current letter not matching the word, or the current letter is being reused
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False
            
            # add the current row and column to the path set
            path.add((r, c))

            # run the recursive DFS function on all four adjacent cells and save their return values to res
            res = (dfs(r + 1, c, i + 1) or 
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or 
                   dfs(r, c - 1, i + 1))

            # remove the current row and column from the path set
            path.remove((r, c))

            # return res
            return res
        
        # run the DFS function on every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):

                # if the DFS function returns true, then the word was found in the grid
                if dfs(r, c, 0):
                    return True
        
        # if the code reaches this point, the word was not found in the grid 
        return False