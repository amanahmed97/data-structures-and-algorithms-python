"""
https://leetcode.com/problems/longest-palindromic-substring/description/
Given a string s, return the longest
palindromic
substring
in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"



Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.


"""

from typing import *


class Solution1:
    def longestPalindrome(self, s: str) -> str:
        pal = ""

        for i in range(len(s)):
            for l, r in ((i, i), (i, i + 1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r - l + 1) > len(pal):
                        pal = s[l:r + 1]
                    l -= 1
                    r += 1

        return pal

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd pals
            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    res = s[l:r + 1]
                l -= 1
                r += 1
            # even pals
            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    res = s[l:r + 1]
                l -= 1
                r += 1

        return res