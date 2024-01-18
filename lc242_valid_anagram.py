# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # primitive counting method using hash maps
        # if lengths of strings are not equal, cannot be an anagram
        if len(s) != len(t):
            return False
        
        # create two hash maps
        hmS, hmT = {}, {}

        # iterate through both strings and count each letter occurrence
        for i in range(len(s)):
            hmS[s[i]] = 1 + hmS.get(s[i], 0)
            hmT[t[i]] = 1 + hmT.get(t[i], 0)
    
        # iterate through a hash map and check if the letter occurrence matches
        for c in hmS:
            if hmS[c] != hmT.get(c, 0):
                return False
            
        # if code reaches this point, the two strings must have identical letter occurrence - thus anagrams
        return True
    
        # alternatively, can also use counters to count each letter occurrence
        # return Counter(s) == Counter(t)

        # easiest solution is to sort strings and check if equal
        # return sorted(s) == sorted(t)
    

