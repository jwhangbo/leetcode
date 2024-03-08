# 90. Subsets II
# https://leetcode.com/problems/subsets-ii/

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # naive approach is to approach the same way as problem 78, but duplicates will cause an issue
        # instead, a small optimization can be made to first sort the given list, then set the pointer to skip all duplicate values
        # with this approach, time complexity will be O(n * 2^n)
        # sorting will also add O(nlogn), but the time complexity of creating the subsets will be far higher

        # initialize a list to store the results, which are the subsets of the given nums list
        res = []

        # sort nums beforehand
        nums.sort()

        # create the recursive backtrack function, using the index and subset as parameters
        def backtrack(i, subset):

            # create a base case for the recursive function by checking if i equals the length of nums
            if i == len(nums):
                res.append(subset[::])
                return
            
            # decision for all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # decision for all subsets that don't include nums[i]
            # skip all duplicate values by checking if the index is in bound and if the values are duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        
        # run the backtrack function on the first index
        backtrack(0, [])

        # if the code reaches this point, all subsets would have been found
        return res