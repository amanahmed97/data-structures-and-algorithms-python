"""
https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]



Constraints:

    1 <= n <= 8
"""
from typing import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(l, r, p):
            if len(p) == 2 * n:
                res.append(p)
                return

            if l < n:
                backtrack(l + 1, r, p + '(')
            if r < l:
                backtrack(l, r + 1, p + ')')

        backtrack(0, 0, '')
        return res