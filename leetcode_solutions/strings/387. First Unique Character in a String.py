"""
https://leetcode.com/problems/first-unique-character-in-a-string/description/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1



Constraints:

    1 <= s.length <= 105
    s consists of only lowercase English letters.
"""
from typing import *

class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniq = []
        suniq = set()

        for c in s:
            if c in uniq:
                uniq.remove(c)
            elif  c not in suniq:
                uniq.append(c)
                suniq.add(c)
        print(uniq)
        return s.index(uniq[0]) if uniq else -1


class Solution1:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1