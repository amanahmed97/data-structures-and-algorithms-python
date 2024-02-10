"""
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

from typing import *


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        op = [0] * len(temperatures)
        tlen = len(temperatures)
        stack = [(0, temperatures[0])]

        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                p, t = stack.pop()
                op[p] = i - p
            stack.append((i, v))

        return op


class SolutionTLE:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        op = [0] * len(temperatures)
        tlen = len(temperatures)

        for i in range(tlen):
            t = temperatures[i]
            for j in range(i + 1, tlen):
                if temperatures[j] > t:
                    op[i] = j - i
                    break

        return op