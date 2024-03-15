# 703. Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/

from typing import List
import heapq
class KthLargest:
    # brute force approach is to use lists, but sorting and adding values to the list will have a high time complexity
    # to optimize the approach, a min heap of size k can be used instead
    # this would bring the time complexity down to O(n * logn) for the init, but O(logn) for the add function

    def __init__(self, k: int, nums: List[int]):

        # initialize a min heap of size k by converting the list to a heap
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)

        # pop from the heap until the size is k
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
                
    def add(self, val: int) -> int:

        # push the value to the heap and pop from the heap until the size is k
        # this is necessary as the heap may be initialized to be less than size k, which means no pop is needed
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        # return the first value of the heap, which will be the Kth largest value
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)