# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # primitve method is to brute force every possible area
        # this will be O(n^2) time complexity 

        # res = 0
        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         area = (r - 1) * min(height[l], height[r])
        #         res = max(res, area)
        # return res
        
        # this method can be optimized using two pointers
        # begin by taking the leftmost and rightmost heights and calculate the area
        # if the left height is greater than the right height, decrement the right pointer to possibly find a larger area
        # if the right height is greater than the left height, increment the left pointer to possibly find a larger area
        # continue until the left and right pointers meet
        # this will be O(n) time complexity since every value is iterated through once

        # initialize a number to track the largest area found so far
        res = 0

        # create the pointers for left and right
        l, r = 0, len(height) - 1

        # create a while loop to iterate each height
        while l < r:

            # calculate the area using the two pointers
            area = (r - 1) * min(height[l], height[r])

            # compare against the existing area and save the larger of the two
            res = max(res, area)

            # if the left height is greater than the right height, decrement the right pointer to possibly find a larger area
            if height[l] > height[r]:
                r -= 1
            
            # if the right height is greater than the left height, increment the left pointer to possibly find a larger area
            # since the elif and else will have the same logic, can condense into an else statement
            else:
                l += 1
        
        # if code reaches this point, the largest area in the list of heights will have been found
        return res