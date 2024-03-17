# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # using a min heap is the ideal approach to the problem

        # initialize a min heap by calculating the distance from the origin for all points and converting the list to a heap
        min_heap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            min_heap.append([dist, x, y])
        heapq.heapify(min_heap)

        # initialize a results list to store all k closest points to origin
        res = []

        # iterate until k is found
        while k > 0:

            # pop from the heap and append the xy coordinates to res
            dist, x, y = heapq.heappop(min_heap)
            res.append([x, y])

            # decrement k
            k -= 1

        # if the code reaches this point, all k closest points to origin will have been found
        return res