"""
https://leetcode.com/problems/palindromic-substrings/description/

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".



Constraints:

    1 <= s.length <= 1000
    s consists of lowercase English letters.
"""

from typing import *


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.countPals(i, i, s)
            count += self.countPals(i, i + 1, s)

        return count

    def countPals(self, l, r, s):
        ctr = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            ctr += 1

        return ctr