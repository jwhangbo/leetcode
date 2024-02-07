# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/

import math
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # primitive method is to calculate the maximum guaranteed rate Koko must eat to be within the hour constraint
        # this can be calculated by using the largest pile of bananas in the list
        # afterwards, the algorithm can brute force by checking every rate to find the minimum rate that stays within the hour constraint
        # this would run at O(max(p) * p), where p is the number of piles
        
        # binary search can be used for the last portion of the primitve method to optimize the time complexity
        # this would instead run at O(log(max(p)) * p)

        # initialize the two pointers for the slowest and fastest rates
        # note that the slowest rate cannot be 0; therefore, it must be 1
        l, r = 1, max(piles)

        # initialize a number to track the minimum rate required, which defaults to the maximum rate
        res = r

        # loop until the left pointer becomes greater than the right pointer
        while l <= r:
            
            # set the middle pointer to the sum of the left and right pointers, then divided by 2
            k = (l + r) // 2

            # initialize the number of hours needed to finish the piles to 0
            hours = 0

            # iterate through the list of banana piles to calculate the total number of hours
            # the ceil() method is used to round up decimals to integers
            for p in piles:
                hours += math.ceil(p / k)
            
            # if the hours with current rate is less or equal to the given hour constraint, recalculate the right pointer to k - 1
            # however, since a new minimum rate may have been found, check against the existing minimum rate
            if hours <= h:
                res = min(res, k)
                r = k - 1
            
            # if not, recalculate the left pointer to k + 1 to possibly find a lower number of hours
            else:
                l = k + 1
        
        # if code reaches this point, the minimum rate that meets the given constraint will have been found
        return res