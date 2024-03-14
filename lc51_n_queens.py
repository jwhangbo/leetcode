# 51. N-Queens
# https://leetcode.com/problems/n-queens/

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # backtracking is the optimal brute force approach to this problem
        # by iterating down each row of the board, each valid queen position can be recursively found

        # initialize three sets to track the column, positive and negative diagonals of the board
        # this is used to prevent putting queens on invalid row-column pairs
        # the positive diagonal is calculated using row + col, while the negative diagonal is row - col
        col = set()
        pos_diag = set()
        neg_diag = set()

        # initialize a list to store the results, which are distinct board state solutions
        res = []

        # initialize a board using the given n value for the row and columns
        board = [["."] * n for i in range(n)]

        # create the recursive backtrack function, using the row as the parameter
        def backtrack(r):

            # create a base case for the recursive function by checking if r equals n
            if r == n:

                # convert the list to a string and append it to res
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # iterate through each column of the row
            for c in range(n):

                # decision to not place the queen at the row-column pair
                # check if the column, positive and negative diagonals are already used
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # decision to place the queen at the row-column pair
                # update the column, positive and negative diagonal sets and set the queen
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                # call the backtrack function on the next row
                backtrack(r + 1)

                # remove the row-column pair from the column, positive and negative diagonal sets and remove the queen
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
        
        # run the backtrack function on the first row
        backtrack(0)

        # if the code reaches this point, all distinct board state solutions will have been found
        return res