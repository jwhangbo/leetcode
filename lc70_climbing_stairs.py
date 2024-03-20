# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # a DFS approach would work, but the time complexity would be O(2^n)
        # instead, this could be optimized to use dynamic programming (DP)
        # with a bottom-up DP approach, the time complexity can be reduced to O(n)
        # this is possible due to removing all duplicate work when iterating through the tree via DFS using memoization
        
        # the advantage of starting with the base case is that the next value can be calculated based on the previous two
        # this is conceptually identical to the Fibonacci sequence
        # moreover, instead of storing a list to track all values, two pointers can be used instead

        # initialize two pointers for the first two base cases
        # these will always be 1 and 1, no matter what the value of n is
        one, two = 1, 1

        # loop for n - 1 times
        for i in range(n - 1):
            
            # temporarily store the value of one
            temp = one

            # update one to be the sum of one and two
            one = one + two

            # update two to be the previous one
            two = temp
        
        # if the code reaches this point, one will be pointing to the number of different ways to climb stairs of n steps
        return one