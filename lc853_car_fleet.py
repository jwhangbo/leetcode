# 853. Car Fleet
# https://leetcode.com/problems/car-fleet/

from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # note that the positions and targets are a system of linear equations
        # if two cars collide, the speed will be reduced down to the car with a higher intial position
        # therefore, it would make sense to sort the positions and its respective speed
        # furthermore, it would also make sense to approach the sorted list of positions and speeds in reverse
        # this is to bypass the condition of what occurs when two cars collide - starting from high to low catches all cases
        # a stack can be used to enforce the LIFO method when iterating through the reverse sorted list
        # if the current car's time to reach the target is lower than the previous car's time, the latter should be popped
        # after the stack is iterated through, the length of the stack would represent the number of car fleets

        # while iterating through the list would be O(n) time complexity, the sort would raise it to O(nlogn)
        # the memory complexity will also be O(n) as a stack is used to possibly account for all cars

        # create the list of cars with their positions and speeds paired up
        # the zip() method is used to link the position to the speed 
        pair = [[p, s] for p, s in zip(position, speed)]

        # create the stack
        stack = []

        # iterate through the car pairs list in reverse
        for p, s in sorted(pair)[::-1]:
            
            # push the time it takes for the car to reach the target to the stack
            stack.append((target - p) / s)

            # check if there are at least two times pushed to the stack and if the current car will reach the target before the car ahead
            if len(stack) >= 2 and stack[-1] <= stack[-2]:

                # if both conditions are true, pop from the stack as the cars would collide
                # this also ensures that the car ahead will always be the point of reference in future comparisons
                stack.pop()
        
        # if code reaches this point, the list of car pairs will have been iterated through
        # therefore, the length of the stack would represent the number of car fleets
        return len(stack)