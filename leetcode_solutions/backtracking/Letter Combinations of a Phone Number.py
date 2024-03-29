"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]



Constraints:

    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].
"""

from typing import *


class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        combo = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        op = []

        def backtrack(i, s):
            if i == len(digits):
                op.append(s)
                return

            for l in combo[int(digits[i])]:
                backtrack(i + 1, s + l)

        backtrack(0, '')
        return op if digits else []


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        global letter
        letter = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }

        global op
        op = []

        if not digits:
            return op

        self.solver(digits, 0, '')
        return op

    def solver(self, digits, index, path):
        if index >= len(digits):
            op.append(path)
            return
        for i in letter[digits[index]]:
            self.solver(digits, index + 1, path + i)