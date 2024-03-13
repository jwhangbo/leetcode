# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # this problem must be brute forced in order to solve, but backtracking can be used
        # the time complexity will be O(n * 4^n), where n is the length of the string

        # initialize a list to store the results, which are letter combinations of a phone number
        res = []

        # initialize a hash map containing all digits to characters
        digit_to_char = { "2": "abc",
                          "3": "def",
                          "4": "ghi",
                          "5": "jkl",
                          "6": "mno",
                          "7": "qprs",
                          "8": "tuv",
                          "9": "wxyz" }
        
        # create the recursive backtrack function, using the index and current string as the parameters
        def backtrack(i, curr_str):

            # create a base case for the recursive function by checking if the length of curr_str is equal to digits
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
            
            # iterate through the string of characters associated with the digit and call the backtrack function on each character
            for c in digit_to_char[digits[i]]:
                backtrack(i + 1, curr_str + c)

        # only run the backtrack function if digits is a non empty string
        if digits:
            backtrack(0, "")

        # if the code reaches this point, all letter combinations of the given phone number will have been found
        return res