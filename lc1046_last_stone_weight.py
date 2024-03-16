# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/

from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # a max heap can be used for the approach, but Python does not natively support max heaps
        # instead, a min heap can be used by converting all of the stone weights to its negative values

        # initialize a min heap by converting the list to a heap
        # the list will convert all of the weights to negatives
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # loop until only one weight remains in the heap
        while len(stones) > 1:

            # take the two heaviest weights, which will be the first two values of the min heap
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            # if the second weight is less than the first weight, the first stone will have a new weight first - second
            if second > first:
                heapq.heappush(stones, first - second)

        # add 0 to stones to behave as the default for the case of all stones breaking
        stones.append(0)

        # if the code reaches this point, the last stone weight will be the first value of the heap
        # taking the absolute value of the weight will convert the value to a positive if needed
        return abs(stones[0])