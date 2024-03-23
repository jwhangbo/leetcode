# 198. House Robber
# https://leetcode.com/problems/house-robber/

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP can be used to optimize the approach
        # note that to calculate the maximum money earned, just the previous two rob values can be tracked
        # rob values are then calculated by taking the maximum between the option of using rob1 + n, or rob2
        # this will guarantee that after the nums list is fully incremented, rob2 should return the maximum amount of money earned

        # initialize the first two rob values as 0, since no houses have been robbed yet
        rob1, rob2 = 0, 0

        # increment through each house
        for n in nums:

            # at each house, take the maximum between rob1 + n, or rob2 as this will reflect the requirement of adjacent houses
            tmp = max(n + rob1, rob2)

            # set rob1 to rob2, and rob2 to tmp, which will return the maximum value so far
            rob1 = rob2
            rob2 = tmp
        
        # if the code reaches this point, rob2 will contain the maximum amount of money earned
        return rob2