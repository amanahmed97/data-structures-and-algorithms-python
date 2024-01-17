"""
https://leetcode.com/problems/palindrome-partitioning/description/

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]



Constraints:

    1 <= s.length <= 16
    s contains only lowercase English letters.
"""

from typing import *


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, subset = [], []

        def dfs(i):
            if i == len(s):
                res.append(subset[::])
                return

            for j in range(i, len(s)):
                if self.isPal(s, i, j):
                    subset.append(s[i:j + 1])
                    dfs(j + 1)
                    subset.pop()

        dfs(0)
        return res

    def isPal(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
