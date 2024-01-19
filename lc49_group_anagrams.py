# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # primitive method would consist of sorting each str in list
        # this would be O(m * nlogn) time, m = length of str list and n = avg str len

        # cleaner method is to use more memory to reduce time
        # create a hash map to track the anagrams
        # defaultdict is used to avoid KeyError for missing keys - will default to empty list instead
        hm = defaultdict(list)

        # iterate through each str in the list
        for s in strs:

            # create a list to count all 26 characters for lower case alphabet and default to 0
            count = [0] * 26

            # iterate through each letter in str
            for c in s:

                # increment the count for the respective element
                # subtracting it by ord("a") ensures that the indices align (i.e. a = 0, b = 1, etc.)
                count[ord(c) - ord("a")] += 1
            
            # use the above list as a key for the hash map and append the str to it
            # this ensures that only the strs that are anagrams will be grouped together
            # the tuple conversion for count is needed as a list is mutable, but a tuple is immutable
            # in Python, the list of a dict can only have keys of immutable type (i.e. string, number)
            hm[tuple(count)].append(s)
        
        # the keys are not needed for the final output, so only return the values
        return hm.values()
