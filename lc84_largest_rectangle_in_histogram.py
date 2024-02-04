# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/

from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # while iterating through the list of heights, note that the area can only extend if the next height >= current height
        # if current height < next height, a maximum area for the current height will be reached
        # a stack can be used to enforce the LIFO method when iterating through the list of heights and their indices
        # whenever the current height < next height, the stack can be popped to stop 'tracking' the height
        # however, the starting index should reference the current height on the next height
        # this is due to the fact that the 'reduced' height can still be extended
        # i.e. if the list is [2, 2, 2, 1], once the algorithm reaches the 1, the height of 2 can be popped
        # however, the left to right area from index 0 to the end of the list can still extend, such as [2, 2, 2, 1, 5]

        # moreover, by the end of the iteration, some of the heights may still be in the stack
        # these will be the heights that can reach to the end of the histogram
        # therefore, they should all be accounted for by calculating the width of the area as the index to the end of the histogram

        # this algorithm will be O(n) time complexity as all heights will only be pushed and popped once at most
        # it will also be O(n) worst case memory complexity as the stack can at worst be the size of the heights list

        # initialize a number to track the maximum area found so far
        max_area = 0

        # create the stack that will store the (index, height) pair
        stack = []

        # iterate through the list of heights
        for i, h in enumerate(heights):

            # initalize the starting index
            start = i

            # pop the stack whenever the height of the top of the stack is greater than the current iterated height
            # whenever the stack is popped, calculate the max area and check against the existing max area
            # shift the starting index to the one from the popped index-height pair
            while stack and stack[-1][1] > h:
                popped_i, popped_h = stack.pop()
                max_area = max(max_area, popped_h * (i - popped_i))
                start = popped_i

            # push the index-height pair to the stack
            # note that the starting index should be referenced in case it got updated in the while loop
            stack.append((start, h))
        
        # iterate through the list of pairs in the stack and calculate the max area to check against the existing max area
        # the end of the histogram will be how far the width of the area will extend to
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        # if code reaches this point, the max area of the largest area in the histogram will have been found and saved
        return max_area