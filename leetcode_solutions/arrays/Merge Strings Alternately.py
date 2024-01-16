"""
https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d



Constraints:

    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.
"""

from typing import *


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        res = ""

        while p1 < len(word1) and p2 < len(word2):
            if (p1 + p2) % 2 == 0:
                res += word1[p1]
                p1 += 1
            else:
                res += word2[p2]
                p2 += 1

        while p1 < len(word1):
            res += word1[p1]
            p1 += 1

        while p2 < len(word2):
            res += word2[p2]
            p2 += 1

        return res
