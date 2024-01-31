# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # reverse polish notation is to sequentially iterate through a list of tokens
        # whenever an operator appears, apply it to the previous two integer values
        # i.e. ["1", "3", "+"] would be evaluated to 1 + 3
        # however, if the list of tokens extended to ["1", "3", "+", "4", "*"], 4 would be multiplied by the result of 1 + 3
        # knowing this pattern, a LIFO method is best suited to process the tokens
        
        # create the stack
        stack = []

        # iterate through each token in the list
        for t in tokens:

            # check if the token is an addition operator
            if t == "+":
                # pop the stack twice and push the result back to the stack
                stack.append(stack.pop() + stack.pop())

            elif t == "-":
                # pop the stack twice and push the result back to the stack, but note that the order matters
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            elif t == "*":
                # pop the stack twice and push the result back to the stack
                stack.append(stack.pop() * stack.pop())

            elif t == "/":
                # pop the stack twice and push the result back to the stack, but note that the order matters
                # moreover, the int() method is used to ensure that the result truncates towards zero
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))

            else:
                # if the token is not an operator, it must be an integer, so it can be pushed to the 
                # the token must be converted from string to integer
                stack.append(int(t))
        
        # if code reaches this point, there must be only one integer left in the stack
        return stack[0]