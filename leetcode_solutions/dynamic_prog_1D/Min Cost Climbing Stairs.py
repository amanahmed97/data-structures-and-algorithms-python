"""
https://leetcode.com/problems/min-cost-climbing-stairs/description/

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.



Constraints:

    2 <= cost.length <= 1000
    0 <= cost[i] <= 999


"""

from typing import *


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # recursion

        dp = []

        for i, v in enumerate(cost):
            if i < 2:
                dp.append(v)
            else:
                dp.append(cost[i] + min(dp[i - 1], dp[i - 2]))

        return min(dp[len(cost) - 1], dp[len(cost) - 2])

    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        # recursion

        def recurse(i: int, scost: int, cost: List[int]):
            if i > len(cost) - 1:
                return scost

            if i != -1:
                scost += cost[i]

            s1 = recurse(i + 1, scost, cost)
            s2 = recurse(i + 2, scost, cost)

            return s1 if s1 < s2 else s2

        return recurse(-1, 0, cost)


'''
def recurse(i: int, scost: int, cost: List[int]):
            if i == len(cost)-1:
                return scost

            scost += cost[i]

            if i == len(cost)-2:
                return recurse(i+1, scost, cost)
            elif cost[i+1] < cost[i+2]:
                return recurse(i+1, scost, cost)
            else:
                return recurse(i+2, scost, cost)

'''
