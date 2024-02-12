"""
https://leetcode.com/problems/consecutive-numbers-sum/description/

Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.



Example 1:

Input: n = 5
Output: 2
Explanation: 5 = 2 + 3

Example 2:

Input: n = 9
Output: 3
Explanation: 9 = 4 + 5 = 2 + 3 + 4

Example 3:

Input: n = 15
Output: 4
Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5



Constraints:

    1 <= n <= 109
"""


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        i = 1
        triangleNum = 1

        while triangleNum <= n:
            if (n - triangleNum) % i == 0:
                ans += 1
            i += 1
            triangleNum += i

        return ans
