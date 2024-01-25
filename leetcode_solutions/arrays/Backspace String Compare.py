"""
https://leetcode.com/problems/backspace-string-compare/description/

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
"""

# Two pointers approach also possible

from typing import *


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = []
        ts = []

        for c in s:
            if c != "#":
                ss.append(c)
            elif len(ss) > 0:
                ss.pop()
        for c in t:
            if c != "#":
                ts.append(c)
            elif len(ts) > 0:
                ts.pop()

        ss = ''.join(ss)
        ts = ''.join(ts)

        return True if ss == ts else False
