# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # primitive method is to brute force by iterating each number until target is found
        # this will be O(n^2) worst case time complexity
        
        # the primitive method does not take advantage of the fact that the given list is sorted
        # two pointers can be used to sum the leftmost and rightmost numbers in the list
        # if the sum is greater than the target, then the sum should be decreased by decrementing the right pointer
        # if the sum is less than the target, then the sum should be increased by incrementing the left pointer
        # if neither are true, then the pointers sum up to the target
        # this will be O(n) worst case time complexity with no extra memory needed

        # create the pointers for left and right
        l, r = 0, len(numbers) - 1

        # create a while loop to iterate each character simultaneously from l-r and from r-l
        while l < r:
            
            # get the sum of the numbers from the left and right pointers
            cursum = numbers[l] + numbers[r]

            # if the current sum is greater than the target, decrement the right pointer
            if cursum > target:
                r -= 1
            
            # if the current sum is less than the target, increment the left pointer
            elif cursum < target:
                l += 1

            # if neither is true, the current sum equals the target
            # note that the problem specified that the indices are 1-indexed, so 1 must be added to each index
            else:
                return [l + 1, r + 1]