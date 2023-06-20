"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.



Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104


"""
from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        low = prices[0]

        for p in prices:
            if p < low:
                low = p
            res = max(res,p-low)

        return res

    def maxProfit3(self, prices: List[int]) -> int:
        m = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                m = max(m, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return m
    def maxProfit2(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        if len(prices)<3:
            s = prices[1] - prices[0]
            return s if s>0 else 0
        max=0
        l=0
        r=len(prices)-1

        while l<len(prices)-1:
            if r == l:
                l+=1
                r=len(prices)-1
            if prices[l]>prices[r]:
                r-=1
            elif prices[r]-prices[l] > max:
                max = prices[r]-prices[l]
                r-=1
            else:
                r-=1

        return max

    def maxProfit1(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        if len(prices)<3:
            s = prices[1] - prices[0]
            return s if s>0 else 0
        max=0
        l=0
        r=l+1

        while l<len(prices)-2:
            if r == len(prices):
                l+=1
                r=l+1
            if prices[l]>prices[r]:
                r+=1
            elif prices[r]-prices[l] > max:
                max = prices[r]-prices[l]
                r+=1
            else:
                r+=1

        return max