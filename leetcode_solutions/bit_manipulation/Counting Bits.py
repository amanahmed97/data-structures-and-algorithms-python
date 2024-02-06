"""
https://leetcode.com/problems/counting-bits/description/

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's
in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:

    0 <= n <= 105

Follow up:

    It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
    Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""
from typing import *


class Solution2:
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n+1)]


class Solution:
    def countBits(self, n: int) -> List[int]:
        def onebits(i: int):
            b = 0
            ctr = 0
            while i > 0:
                r = i % 2
                # print(r)
                if r:
                    ctr += 1
                b = b*10 + r
                i = i // 2
            print(b)

            return ctr
                # sum(list(b))

        op = [0] * (n + 1)

        for i, v in enumerate(op):
            op[i] = onebits(i)

        return op

s = Solution()
a = s.countBits(7)
print(a)

class Solution1:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
