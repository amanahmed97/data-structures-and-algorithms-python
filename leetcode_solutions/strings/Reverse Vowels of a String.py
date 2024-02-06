"""
https://leetcode.com/problems/reverse-vowels-of-a-string/description/

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"



Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.
"""

from typing import *


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        sv = []
        positions = []
        s = list(s)

        for i, v in enumerate(s):
            if v in vowels:
                positions.append(i)
                sv.append(v)

        # sv = sv[::-1]
        sv.reverse()
        svi = 0
        for p in positions:
            s[p] = sv[svi]
            svi += 1

        return ''.join(s)

    def reverseVowels1(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        sv = []
        positions = []
        new_s = ""

        for i, v in enumerate(s):
            if v in vowels:
                positions.append(i)
                sv.append(v)

        # sv = sv[::-1]
        sv.reverse()
        svi = 0
        for i, v in enumerate(s):
            if i in positions:
                new_s += sv[svi]
                svi += 1
            else:
                new_s += s[i]

        return new_s