# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # primitive approach is to sort nums and find the kth index
        # nums.sort()
        # return nums[len(nums) - k]

        # however, a more well rounded approach is to use the quick select algorithm
        # this is similar to quick sort in terms of using partitions, but the select will not care about sorting
        # instead, the goal is to have the pivot point equal k, which will guarantee that the index will point to the answer
        # the time complexity will be O(2n), which gets simplified to O(n)
        # the time complexity of the quick select approach is not necessarily always better than the primitive approach
        # however, it will be better on average

        # reinitialize k to be the target index of nums
        k = len(nums) - k

        # create a recursive function for the quick select algorithm, with the left and right pointers as the parameters
        def quick_select(l, r):

            # initialize the pivot and p (partition) indices
            # use the rightmost value as the default pivot
            pivot, p = nums[r], l

            # iterate through the list up until the pivot
            for i in range(l, r):

                # if the current value is less than or equal to the pivot, swap their positions
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]

                    # the p pointer must be incremented
                    p += 1
            
            # swap the rightmost value and the p value
            nums[p], nums[r] = nums[r], nums[p]

            # if p is less than k, run quick_select() on the left partition
            if p > k:
                return quick_select(l, p - 1)
            
            # if p is greater than k, run quick_select() on the right partition
            elif p < k:
                return quick_select(p + 1, r)
            
            # else, nums[p] must be the kth largest value in nums
            else:
                return nums[p]
        
        # run quick_select() with default values 0 and the length of nums and return the output
        return quick_select(0, len(nums))