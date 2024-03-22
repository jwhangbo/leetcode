# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # brute force approach is to use two decision trees for starting at either index 0 or index 1
        # instead, similar to problem 70, bottom-up DP can be used to optimize time efficiency to O(n)
        
        # note that by starting with the base case, the list can be decremented
        # in doing so, the algorithm can take the minimum of the two decisions to take 1 or 2 steps
        # for instance, if the list was [10, 15, 20], the provided answer is 15, as one can start from index 1 and take 2 steps
        # instead, the costs can be reinterpreted as [10, 15, 20, 0], where 0 acts as the final step and would cost 0
        # afterwards, by decrementing from the third to last index until index 0, the minimum cost can be calculated
        # at the third to last index, index 1, the value of 15 can either have 20 or 0 added to its cost
        # since 0 is the lesser of the two values, it will be preferred
        # at index 0, the value of 10 can either have 15 or 20 added to its cost, so 15 would be chosen to sum to 25
        # afterwards, comparing between index 0 and index 1 reveals that the latter would have a lower minimum cost

        # add a 0 to the cost list in order to maintain the increment logic
        cost.append(0)

        # loop for len(cost) - 3 times by decrementing throughout the list
        # -3 is used as the starting point can either be index 0 or index 1
        for i in range(len(cost) - 3, -1, -1):

            # calculate the current index as the sum of the current value and the minimum of the two decisions available
            cost[i] += min(cost[i + 1], cost[i + 2])

        # if the code reaches this point, the minimum cost can be found by taking the minimum between index 0 and index 1
        return min(cost[0], cost[1])