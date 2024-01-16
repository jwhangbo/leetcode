# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # primitive method is to brute force by comparing each value against all others
        # this would be O(n^2) time but O(1) space, thus not ideal

        # slightly better approach is to sort all values and check if adjacent values are duplicates
        # this would improve the time to O(nlogn) for avg sorting time but still O(1) space, thus an improvement

        # can trade space for better time by using a hash set
        # time would drop drastically to O(n) but space would also go up to O(n) as a hash set of s size is created
        # create a hash set
        hs = set()

        # iterate through each element in list
        for i in nums:

            # check if element has alraedy been added to hash set, which confirms that the value is a duplicate
            if i in hs:
                return True
            
            # add element to hash set if it doesn't already exist
            hs.add(i)
        
        # if code reaches this point, all elements must be unique
        return False