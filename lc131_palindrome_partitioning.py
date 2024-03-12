# 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/

from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # this problem must be brute forced in order to solve, but backtracking can be used
        # recursive DFS can be used to check every character in the string

        # initialize a list to store the results, which are valid palindrome partitions
        res = []

        # initialize a list to store the current partition
        part = []

        # create the recursive DFS function, using the index as the parameter
        def dfs(i):

            # create a base case for the recursive function by checking if i is equal or greater than the length of s
            if i >= len(s):
                res.append(part.copy())
                return
            
            # iterate through the remaining characters
            for j in range(i, len(s)):

                # check if the current partition between i and j is a valid palindrome
                if self.is_pali(s, i, j):

                    # append the current partition to the part list
                    part.append(s[i:j+1])

                    # run the recursive DFS function on the remaining characters of s
                    dfs(j + 1)

                    # remove the current partition from the part list
                    part.pop()

        # run the DFS function on the first index of s
        dfs(0)
        
        # if the code reaches this point, all palindrome partitions will have been found
        return res
    

    # create a helper function to check if the given partition is a valid palindrome
    def is_pali(self, s, l, r):

        # have i and j act as the left and right pointers, and check if their values are equal
        while l < r:

            # if the left and right values are not equal, return false
            if s[l] != s[r]:
                return False
            
            # increment and decrement the left and right pointers respectively
            l, r = l + 1, r - 1

        # if the code reaches this point, the partition must be a valid palindrome
        return True