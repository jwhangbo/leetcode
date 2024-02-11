# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # similar method as two pointers, but instead of taking the rightmost index, start next to left pointer instead
        # this creates a sliding window solution, where the left and right pointers map out a 'window' of the list
        # this 'window' will then optimize in search of a better solution with each conditional iteration

        # itialize two pointers for the leftmost the following value in the list
        # the left pointer acts as the buy signal while the right pointer acts as the sell signal
        l, r = 0, 1

        # initialize the maximum price found by the sliding window
        max_profit = 0


        # loop until the right pointer becomes greater than the length of the list
        while r < len(prices):

            # if the left pointer's value is less than the right pointer's value, a profit may have been made
            if prices[l] < prices[r]:

                # calculate the profit based on the buy/sell signals and check against the existing max profit
                profit = prices[r] - prices[l]                
                max_profit = max(max_profit, profit)
            
            # else, the window should be slid to use the right pointer as the new buy signal
            # this is due to the fact that if this condition is met, the right pointer's value must be a new local low value
            # therefore, this is the best value to use as the new buy signal, based on the idea of buying low and selling high
            else:
                l = r
            
            # the base case should increment the right pointer by 1 to see if the next sell signal is more profitable
            r += 1

        # if code reaches this point, the maximum profit within the list of prices will have been found
        return max_profit