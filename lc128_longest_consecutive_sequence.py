# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # primitive method is to sort the list and increment through the sorted list to find the longest consecutive sequence
        # this will run at O(nlogn) time due to the requirement of having to sort the list

        # instead, can simplify the problem by attempting to visualize it
        # note that a definition of a start of a sequence can be established - if num is n, n-1 must not be in nums
        # using this definition, an algorithm can be created in order to find the sequence in one pass
        # while iterating through each number in nums, if n-1 is not in nums, check how long the sequence is
        # otherwise, n can be ignored since it cannot be the start of a consecutive sequence
        # since this method only requires one pass, it will run at O(n) time with O(n) memory complexity

        # this is optimized by using a set to quickly check for n-1 existence
        # convert nums into a set
        nset = set(nums)

        # initialize a number to track the length of the longest consecutive sequence
        longest = 0

        # iterate through each number in nums
        for n in nums:

            # check if n-1 is not in the nums set
            if (n-1) not in nset:
                
                # this means n must be a start of a sequence - thus, now keep track of how long it is
                length = 1
                while (n + length) in nset:

                   # increment length if the sequence continues
                    length += 1

                # since loop finished, the sequence was fully tracked - compare against the existing longest length
                longest = max(longest, length)

        # if code reaches this point, nums was fully incremented and the longest consecutive sequence length was found
        return longest 