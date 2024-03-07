# 46. Permutations
# https://leetcode.com/problems/permutations/

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking can be used to generate all possible permutations
        # instead of having a separate DFS function, the permute() function itself will be recursive
        
        # initialize a list to store the results, which are the lists containing the permutations
        res = []

        # create a base case for the recursive function by checking if the length of nums is 1
        # this is based on the logic that if there is only one num left, there is also one permutation
        if (len(nums) == 1):
            return [nums[:]]
        
        # iterate through each num in nums
        for i in range(len(nums)):
            
            # pop the first num
            n = nums.pop(0)

            # get the permutations of the remaining nums
            perms = self.permute(nums)

            # for all permutations, add the popped first num to the results list
            for perm in perms:
                perm.append(n)
            res.extend(perms)

            # add the first num back to nums
            nums.append(n)
        
        # if the code reaches this point, all permutations will have been recursively found
        return res