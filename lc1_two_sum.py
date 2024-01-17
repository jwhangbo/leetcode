# 1. Two Sum 
# https://leetcode.com/problems/two-sum/

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force method would consist of iterating through entire list
        # this would be O(n^2) time

        # cleaner method is to find the two sum in one pass
        # create a hash map to track the nums
        hm = {}

        # iterate through the enumerated list to track indices
        for i, j in enumerate(nums):
        
            # calculate diff by subtracting target from current num
            diff = target - j

            # if this diff already exists in diff, two sum is confirmed to exist in list
            if diff in hm:

                # return the two indices
                return (hm[diff], i)
            
            # add the num to the hash map so that the opposite case may be hit
            hm[j] = i
        
        # if code reaches this point, two sum does not exist in this list - not needed
        return