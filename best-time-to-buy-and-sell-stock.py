#Leetcode #122 Best Time to Buy and Sell Stock

# Say you have an array 'prices' for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
"""
U
   (prices) Input: [7,1,5,3,6,4]
   -> 7
P
    loop over range of array 
        set profit variable
        find min (1) and max (6) item out of the rest
        check if next element is higher than i 
            if it is 
                sell
            else
                check the next item
        return profit
E
R
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                profit += (prices[i+1] - prices[i])
        return profit