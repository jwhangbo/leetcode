# 78. Subsets
# https://leetcode.com/problems/subsets/

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # as the most optimal appoach will be O(n * 2^n) due to the inefficiency, backtracking will be the optimal method

        # initialize a list to store the result and for the current subset
        res = []
        subset = []
        
        # create the recursive DFS function, using the index of the given list as the parameter
        def dfs(i):
            
            # create a base case for the recursive function by checking if index is out of range
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision to not include nums[i]
            subset.pop()
            dfs(i + 1)
        
        # run the DFS function on the first index
        dfs(0)

        # if the code reaches this point, the DFS function would have ran every possibility of the subset
        return res