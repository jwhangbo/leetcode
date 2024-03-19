# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/

from typing import List
from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # using a max heap is the ideal approach to the problem
        # since Python does not natively support max heaps, a min heap can be used with values converted to negatives

        # initialize a counter for all tasks
        count = Counter(tasks)
        
        # initialize a max heap by taking the negative value of each value of the counter and converting the list to a heap
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        # initialize the time as 0
        time = 0

        # initialize a queue to track the next task
        q = deque()

        # loop until either heap or queue have been exhausted
        while max_heap or q:

            # increment the time by 1 for each iteration
            time += 1

            # if the heap is not empty, pop from the heap and increment it
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)

                # if the value exists, append the value to the queue, along with the incremented time
                if cnt:
                    q.append([cnt, time + n])
            
            # if the queue is not empty and the time matches, push the value back to the heap
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        # if the code reaches this point, the least interval to run all tasks will have been found
        return time