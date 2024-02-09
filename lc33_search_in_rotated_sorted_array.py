# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # very similar problem to problem 153, but with a small adjustment
        # as the given list will be rotated, they can be perceived as 2 sorted sublists
        # this allows an optimization from the brute force (O(n)) to an optimized solution (O(logn)) using binary search

        # itialize two pointers for the leftmost and rightmost values in the list
        l, r = 0, len(nums) - 1

        # loop until the left pointer becomes greater than the right pointer
        while l <= r:

            # set the middle pointer to the sum of the left and right pointers, then divided by 2
            m = (l + r) // 2
            
            # check if the middle pointer's value is equal to the target
            if target == nums[m]:
                return m

            # check if the middle pointer's value is greater than or equal to the left pointer's value
            if nums[l] <= nums[m]:

                # this confirms that the portion between the left and middle pointers must be sorted
                # check if the target is in between the left and middle pointers and recalculate the left pointer to middle + 1
                if target > nums[m] or target < nums[l]:
                    l = m + l

                # else, recalculate the right pointer to middle - 1
                else:
                    r = m - 1
            
            else:

                # this confirms that the portion between the middle and right pointers must be sorted
                # check if the target is in between the middle and right pointers and recalculate the right pointer to middle - 1
                if target < nums[m] or target > nums[r]:
                    r = m - l

                # else, recalculate the left pointer to middle + 1
                else:
                    l = m + 1
            
        # if code reaches this point, the target value has not been found in the loop
        return -1