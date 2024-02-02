# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # backtrack approach ensures that both time and memory complexity will be O(n)
        # while iterating through the list of temperatures, remember the previous temperature and its index
        # once used, pop the temperature and index - this will maintain a monotonic decreasing stack
        # this is possible as once a greater temperature is found, the lesser temperature and index will be popped from the stack

        # create the list of results and stack
        # the list of results are initialized w[ith 0 in order to account for the case where no future day is available
        res = [0] * len(temperatures)
        stack = []

        # iterate through each temperature in the list
        # use enumerate to track both the index and the temperature
        for i, t in enumerate(temperatures):

            # check against the top of the stack's temperature and see if a greater value has been found
            # if true, pop the value and compare against the current index to calculate the number of days required to find a warmer temp
            while stack and t > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = (i - stack_idx)
            
            # otherwise, add the temperature and index to the stack
            stack.append([t, i])
        
        # if code reaches this point, all of the number of days required to find a warmer temperature will have been saved to the results list
        return res