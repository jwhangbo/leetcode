# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # primitive method is to brute force and check every value in matrix - this would be O(n * m) time complexity
        # a slightly more optimized method is to use binary search on every row - this would be O(mlogn) time complexity
        # ideally, the method should use the property that each row's start will always be greater than the previous row's end
        # in other words, binary search can be applied to both the rows and the columns - this would be O(log(m * n)) time complexity

        # create constants to store the number of rows and columns in the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # initialize the two pointers for the top and bottom row of the matrix
        top, bot = 0, ROWS - 1

        # loop until the top pointer becomes greater than the bottom pointer
        while top <= bot:

            # set the middle pointer to the sum of the top and bottom pointers, then divided by 2
            row = (top + bot) // 2

            # if the target value is greater than the greatest value in the row, recalculate the top pointer to row + 1
            if target > matrix[row][-1]:
                top = row + 1

            # if the target value is less than the least value in the row, recalculate the bottom pointer to row - 1
            elif target < matrix[row][0]:
                bot = row - 1
            
            # if either case is not reached, the target must be contained in the row, thus break out of the loop
            else:
                break
        
        # check if the loop was broken out due to the top pointer becoming greater than the bottom pointer, thus return False
        if not (top <= bot):
            return False
        
        # calculate the index of the row in order to use for the second binary search
        row = (top + bot) // 2

        # itialize two pointers for the leftmost and rightmost columns in the row
        l, r = 0, COLS - 1

        # loop until the left pointer becomes greater than the right pointer
        while l <= r:

            # set the middle pointer to the sum of the left and right pointers, then divided by 2
            m = (l + r) // 2

            # if the target is greater than the middle pointer's value, recalculate the left pointer to middle + 1
            if target > matrix[row][m]:
                l = m + 1
            
            # if the target is less than the middle pointer's value, recalculate the right pointer to middle - 1
            elif target < matrix[row][m]:
                r = m - 1
            
            # if either cases are not reached, the middle pointer's value must equal the target, thus return True
            else:
                return True
    
        # if code reaches this point, the search could not find the target in the matrix, thus return False
        return False