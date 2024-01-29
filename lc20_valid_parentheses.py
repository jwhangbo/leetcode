# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # given the conditions of what it means to have valid parentheses, it is apparent that a LIFO method is needed
        # therefore, a stack is the ideal data structure for this problem
        # as the algorithm iterates through the string, the following can occur
        # if the character is a closed parantheses and the stack's last element matches as the open parentheses, pop the last element
        # otherwise, add the character to the stack
        # after iterating through the function, the string has valid parentheses if the stack is empty
        # the time complexity of this method will be O(n) since the string will only be iterated once
        # likewise, memory complexity will be O(n) since the worst case is to have every character added to the stack

        # create the stack and the hash map to distinguish if the parentheses is open or closed
        # note that the key is the closed parentheses and the value is the respective open parentheses
        stack = []
        hm = {")": "(", "}": "{", "]": "["}

        # iterate through each character in the string
        for c in s:

            # check if the character is a closed parentheses
            if c in hm:

                # check that the stack's last element matches as the open parentheses
                if stack and stack[-1] == hm[c]:
                    
                    # since a pair is found, pop the last element from the stack
                    stack.pop()
                
                # if both conditions are not met, this string is guaranteed to be invalid parentheses
                else:
                    return False
            
            # otherwise, add the character to the stack
            else:
                stack.append(c)
        
        # if stack is empty, the string is valid; otherwise, it is invalid
        return True if not stack else False