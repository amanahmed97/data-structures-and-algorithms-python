"""
https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
    1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        s = [0] * n
        if n < 3:
            return n

        s[0] = 1
        s[1] = 2

        for i in range(2, n):
            s[i] += s[i - 1] + s[i - 2]

        print(s)
        return s[n - 1]
