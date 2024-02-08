# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # similar to problem 704, binary search can be used to optimize the brute force method
        # this would reduce the time complexity from O(n) to O(logn)
        # however, this particular problem has a rotated sorted array - note that this will not break the sort
        # in other words, once a middle pointer is selected, the following cases can occur
        # if the middle pointer's value is greater than or equal to the left pointer's value, recalculate the left pointer to middle + 1
        # if the middle pointer's value is less than the left pointer's value, recalculate the right pointer to middle - 1
        # this logic works as long as there's a check beforehand to see if the sublist from left to right pointer is sorted
        # if true, check the left pointer's value against the existing minimum value and break out of the loop
        
        # simply put, if the middle pointer's value is greater than or equal to the left pointer's value, the right side may be sorted
        # this is due to the logic that a rotated sorted list will always have a sublist that retains the sorted nature
        # if the middle pointer's value is greater or equal to the left pointer's value, the left side cannot be sorted (TODO)

        # initialize a number to track the minimum value, which defaults to the first value in the list
        res = nums[0]

        # itialize two pointers for the leftmost and rightmost values in the list
        l, r = 0, len(nums) - 1

        # loop until the left pointer becomes greater than the right pointer
        while l <= r:

            # if the left pointer's value is less than the right pointer's value, the sublist must be sorted
            # therefore, check the left pointer's value against the existing minimum value and break out of the loop
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            # set the middle pointer to the sum of the left and right pointers, then divided by 2
            m = (l + r) // 2
            
            # check the middle pointer's value against the existing minimum value
            res = min(res, nums[m])

            # if the middle pointer's value is less than or equal to the left pointer's value, recalculate the left pointer to middle + 1
            if nums[m] >= nums[l]:
                l = m + 1

            # else, recalculate the right pointer to middle - 1
            else:
                r = m - 1
        
        # if code reaches this point, the minimum value in the list will have been found
        return res