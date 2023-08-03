"""
https://leetcode.com/problems/sum-of-two-integers/description/

Given two integers a and b, return the sum of the two integers without using the operators + and -.



Example 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = 2, b = 3
Output: 5



Constraints:

    -1000 <= a, b <= 1000

"""
"""
Java solution is better
"""
from typing import  *

class Solution:
    def getSum(self, a: int, b: int) -> int:
        def add(a, b):
            if not a or not b:
                return a or b
            return add(a ^ b, (a & b) << 1)

        if a * b < 0:
            if a > 0:
                return self.getSum(b, a)
            if add(~a, 1) == b:
                return 0
            if add(~a, 1) < b:
                return add(~add(add(~a, 1), add(~b, 1)), 1)

        return add(a, b)
