# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # a sliding window method can be used to iterate through the string in order to find the length of the longest substring
        # using a set to track the characters, the left pointer would shift whenever a duplicate is encountered
        # this ensures that both the time and memory complexity will be O(n)

        # create a set to track unique characters
        char_set = set()

        # initialize the left pointer at the leftmost character of the string
        l = 0

        # initialize the length of the longest substring, which defaults to 0
        res = 0

        # iterate through the length of the string, acting as the right pointer for the sliding window
        for r in range(len(s)):

            # check if the right pointer's character is already in the set that tracks unique characters
            while s[r] in char_set:

                # remove the left pointer's character
                char_set.remove(s[l])
                
                # shift the left pointer until a unique character can be entered into the set
                l += 1
            
            # if the right pointer's character is not already in the set that tracks unique characters, add it to the set
            char_set.add(s[r])

            # calculate the current length of the substring and check against the existing length of the longest substring
            res = max(res, r - l + 1)

        # if code reaches this point, the length of the longest substring will have been found
        return res