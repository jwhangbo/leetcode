# 704. Binary Search
# https://leetcode.com/problems/binary-search/

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search is a divide-and-conquer search algorithm that has O(logn) time complexity
        # the approach is to intialize two pointers for the leftmost and rightmost values

        # since the given list is sorted, the following cases can occur
        # if the middle pointer's value is less than the target, all of the values from the middle to the right pointers will not work
        # if the middle pointer's value is greater than the target, all of the values from the left to the middle pointers will not work
        # therefore, if either case occurs, half of the list can be assumed to not contain the target
        # the middle pointer will become the new left (middle + 1) or right (middle - 1) pointer respectively
        # this process will be repeated until the left pointer becomes greater than the right pointer
        # if the middle pointer never equals the target for any iteration, the target must not exist in the list

        # this algorithm is logarithmic (i.e. 16 values -> 8 -> 4 -> 2 -> 1 after each iteration)

        # itialize two pointers for the leftmost and rightmost values in the list
        l, r = 0, len(nums) - 1

        # loop until the left pointer becomes greater than the right pointer
        while l <= r:

            # set the middle pointer to the sum of the left and right pointers, then divided by 2
            # integer division is used to avoid having decimals
            # for other languages, calculating the middle pointer like this may result in an overflow
            # to mitigate this, the middle pointer can be alternatively calculated by l + ((r - l) // 2)
            # this method will not overflow since instead of possibly adding two large numbers, subtraction is used instead
            m = (l + r) // 2

            # if the middle pointer's value is less than the target, recalculate the left pointer to middle + 1
            if nums[m] < target:
                l = m + 1
            
            # if the middle pointer's value is greater than the target, recalculate the right pointer to middle - 1
            elif nums[m] > target:
                r = m - 1
            
            # if either cases are not reached, the middle pointer's value must equal the target and can return the index
            else:
                return m
        
        # if code reaches this point, the search could not find the target in the list
        return -1