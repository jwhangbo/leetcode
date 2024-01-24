# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # primitive method is to use Python's built in methods to convert the string to the correct format and check against the reverse
        # newstr = ""
        # for c in s:
        #     if c.isalnum():
        #         newstr += c.lower()
        # return newstr == newstr[::-1]

        # however, two pointers can be used to reduce memory complexity to O(1) by not needing to save to another string
        # moreover, a function can be implemented to replicate the .isalnum() method
       
        # create the pointers for left and right
        l, r = 0, len(s) - 1

        # create a while loop to iterate each character simultaneously from l-r and from r-l
        # make sure that the pointers do not cross each other
        while l < r:

            # add another while loop to check if the character is alphanumeric
            # this loop still requires the check for pointers crossing as it is within a different scope
            while l < r and not self.alphanum(s[l]):

                # increment the l pointer by 1 until it reaches a valid alphanumeric character
                l += 1
            
            # repeat the loop for the right pointer
            while r > l and not self.alphanum(s[r]):
                r -= 1

            # check if the left pointer character matches the right pointer
            if s[l].lower() != s[r].lower():

                # since they do not match, the string cannot be a palindrome
                return False

            # increment both pointers by 1 to check for the next character
            l, r = l + 1, r - 1
        
        # if code reaches this point, the string must be a palindrome
        return True
    
    # check if a character is alphanumeric by seeing if the ASCII code is within expected ranges
    def alphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))