# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # primitive method is to sort counter for nums and pop out k times for most frequent elements
        # this is slightly wasteful since the whole counter does not need to be sorted as it's only top k
        # this would also be O(nlogn) worst case time complexity

        # alternatively, can use a max heap and pop out exactly k times - popping from heap would be O(logn)
        # this would be O(klogn), which can be slightly more efficient if k < n

        # ideal method would be in linear time, O(n), using a variant of bucket sort
        # traditional bucket sort would take the max value from the list and create a list from 0 to max
        # each index acts as a bucket and tracks which value i occurs x many times
        # i.e. if list is [1, 1, 1, 2], the bucket would have index 1 at 3 and index 2 at 
        # this would not be linear time, as it's unbounded (i.e. [1, 2, 1000] means the list would be len 1000 despite 3 values)

        # the twist is to flip the index and counter - find the len of the list and create a list from 0 to len
        # each index acts as a counter and tracks which value x occurs i many times
        # this works because even if every value in the list is the same, it would just end up matching the 
        
        # create a hash map to track the nums
        hm = {}

        # create a list of lists to sort the frequency of nums, with the list len equal to len of nums
        frq = [[] for i in range(len(nums) + 1)]

        # iterate through the list to count the frequency of each num
        for n in nums:
            hm[n] = 1 + hm.get(n, 0)

        # iterate through the hash map to sort the frequency of nums
        # .items() method is used as key-value pair is needed - number and count
        for n, c in hm.items():
            frq[c].append(n)
        
        # create an empty list to track top k frequent elements
        res = []

        # iterate through the list that sorted the frequency of nums and descend from max length
        for i in range(len(frq) - 1, 0, -1):

            # a second iteration is needed to go through each bucket, since a bucket can contain multiple values
            for n in frq[i]:

                # since number exists in the bucket and guaranteed to be top k frequent, append to res
                res.append(n)
        
                # return when k number of elements have been added to res
                if len(res) == k:

                    # no outer return is needed based on this problem's constraints
                    return res