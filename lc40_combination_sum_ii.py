# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # similar to problem 90, where a sorted candidates list will solve the issue of duplicates; the time complexity will be O(2^n)

        # initialize a list to store the results, which are the combinations that sum to the target of the given candidates list
        res = []

        # sort candidates beforehand
        candidates.sort()

        # create the recursive backtrack function, using the current combination, position and target as parameters
        def backtrack(curr, pos, target):
            
            # create a base case for the recursive function by checking if the current target equals 0
            if target == 0:
                res.append(curr.copy())
            
            # create another base case for the recursive function by checking if the current target is equal than or less than 0
            # for this case, the tree does not need to continue, so return is used to stop it
            if target <= 0:
                return
            
            # initialize a prev variable as -1 to guarantee that it gets set during the first iteration
            prev = -1
            
            # iterate from the current position to the end of the candidates list
            for i in range(pos, len(candidates)):

                # skip all duplicates
                if candidates[i] == prev:
                    continue

                # decision for all combinations that include candidates[i]
                curr.append(candidates[i])
                backtrack(curr, i + 1, target - candidates[i])
                curr.pop()

                # set prev to the current candidate to prevent another tree from being created on the second iteration of the loop
                prev = candidates[i]
        
        # run the backtrack function on the first index
        backtrack([], 0, target)

        # if the code reaches this point, all unique combinations that sum to the target will have been found
        return res