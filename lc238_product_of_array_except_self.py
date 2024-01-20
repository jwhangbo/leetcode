# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # constraint prevents easiest method of taking the product of all nums and dividing on each element
        # also includes constraint to have the algorithm run at O(n) time
        
        # can do the following prefix/postfix method into two separate lists and would still maintain O(n) time
        # however, memory would be also O(n) - this can be reduced to O(1) by using two pass method
        # first pass is left to right to calculate and initalize all of the prefix values
        # second pss is right to left to take the product of the prefix to find product of array except self

        # create a list to multiply the prefixes to postfixes
        res = [1] * len(nums)
        
        # begin by tracking the prefix of all elements - take the product of all elements before it
        # initialize as 1
        prefix = 1
        for i in range(len(nums)):
            
            # set the res index to the prefix 
            res[i] = prefix

            # take the product of the existing prefix to the current element
            prefix *= nums[i]
        
        # do the same for the postfix, but this must be done by iterating in reverse
        # initialize as 1
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):

            # set the res index to the postfix - prefix already set, so need to take the product
            res[i] *= postfix

            # take the product of the existing postfix to the current element
            postfix *= nums[i]
        
        # return the array
        return res