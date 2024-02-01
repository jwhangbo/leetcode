# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # note that in order to generate well-formed parentheses, the following must be true when generating combinations:
        # 1. the total number of parentheses must equal to n*2, where n are open and n are closed
        # 2. open parentheses can be pushed as long as condition 1 is met and the total is less than n
        # 3. closed parentheses can only be pushed if the current number of open parentheses is greater than closed parentheses
        # by this logic, a backtracking approach is ideal

        # i.e. if n = 2, the following will occur
        # ["("] <- the first parenthesis must always be open, as any combination starting with a closed parentheses will be invalid
        # ["(", ")"] or ["(", "("] <- both open and closed parentheses can be pushed as they meet conditions 2 and 3
        # ["(", ")", "("] or ["(", "(", ")"] <- the first sequence does not meet condition 2 and the latter does not meet condition 3
        # ["(", ")", "(", ")"] or ["(", "(", ")", ")"] <- the first sequence does not meet condition 3 and the latter does not meet condition 2
        # at this point, all 3 conditions have been met, so when n = 2, these are the possible valid parentheses combinations

        # create the stack and the results list to return at the end of the backtrack
        stack = []
        res = []

        # create a recursive function to backtrack
        def backtrack(open_n, closed_n):
            
            # check if open_n == closed_n == n, which will fulfill condition 1
            # at this point, all possible combinations will have been generated, so join the string and append it to the results list
            if open_n == closed_n == n:
                res.append("".join(stack))
                return

            # check if the current open_n is less than n, fulfilling condition 2
            if open_n < n:
                
                # append the open parentheses and backtrack with open_n + 1
                stack.append("(")
                backtrack(open_n + 1, closed_n)

                # update the stack and pop the parentheses as there's only one global stack being used
                stack.pop()

            # check if open_n > closed_n, fulfilling condition 3
            if open_n > closed_n:

                # append the closed parentheses and backtrack with closed_n + 1
                stack.append(")")
                backtrack(open_n, closed_n + 1)

                # update the stack and pop the parentheses as there's only one global stack being used
                stack.pop()
        
        # initialize the backtrack with 0 for open_n and closed_n
        backtrack(0, 0)

        # if code reaches this point, all valid combinations must have been generated and appended as a string to the results list
        return res