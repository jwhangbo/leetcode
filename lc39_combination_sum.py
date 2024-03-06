# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # brute force approach is to create a tree to check for every possible combination
        # however, this approach will not handle duplicate cases - i.e. [2, 3, 3] and [3, 2, 3] would both be found
        # ideally, the optimal approach would avoid having to deal with duplicates
        
        # to do this, the tree can be altered to two sides
        # one side can be for all combinations containing x number of times while the other side will not
        # for instance, if the candidates list was [2, 3, 5], the first split in the tree would use the first candidate
        # the left subtree would contain all combinations with at least one 2
        # the right subtree would contain all combinations with no 2

        # furthermore, continuing down the left subtree would recursively apply the same logic
        # for instance, the next left subtree would contain all combinations with at least two 2s
        # the next right subtree would contain all combinations with only one 2

        # initialize a list to store the results, which are the lists containing the combinations
        res = []

        # create the recursive DFS function, using the index of the candidate, the current variable and the total as parameters
        def dfs(i, cur, total):
            
            # create a base case for the recursive function by checking if the total equals the target
            if total == target:
                res.append(cur.copy())
                return
            
            # create another base case for the recursive function by checking if the total is greater than the target
            # additionally, check if the index is out of bounds in the list of candidates
            if i >= len(candidates) or total > target:
                return
            
            # decision to include candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # decision to not include candidates[i]
            cur.pop()
            dfs(i + 1, cur, total)

        # run the DFS function on the first index
        dfs(0, [], 0)
        
        # if the code reaches this point, the DFS function would have found every combination that sums to the target
        return res