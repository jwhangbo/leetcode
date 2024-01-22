# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # can use hash sets to track if rows or columns contain a duplicate - similar method as problem 217
        # however, the square must also not contain duplicates
        # therefore, another hash set is required to identify which square the row-column pair is located in
        # this can be achieved by using integer division on each row-column pair
        # for instance, the coordinates for the center cell would be [4, 4]
        # dividing each row and column value by 3 ensures that the 9x9 grid can be split into 9 squares
        # thus, [4, 4] would be [(4 // 3), (4 // 3)] = [1, 1], which makes sense as the 9 squares would have indices range from 0 to 2
        # corner cases also work, such as [8, 8] = [2, 2] or [0, 0] = [0, 0]

        # as the problem only asks if the given board state is valid, it is not required to validate any empty 
        # thus, it will run at O(9^2) time

        # create 3 hash sets to keep track of the row, column and square
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # iterate through each row and col - constant value of 9 each
        for r in range(9):
            for c in range(9):
                
                # ignore all empty cells
                if board[r][c] == ".":
                    continue

                # check against all 3 hash sets to check for duplicates and return right away if any are true
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                # add the row-column pair to each respective hash set
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        # if code reaches this point, all conditions met for the sudoku board
        return True