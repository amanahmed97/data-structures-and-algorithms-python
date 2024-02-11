"""
https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/submissions/1171735029/

We have two arrays arr1 and arr2 which are initially empty. You need to add positive integers to them such that they satisfy all the following conditions:

    arr1 contains uniqueCnt1 distinct positive integers, each of which is not divisible by divisor1.
    arr2 contains uniqueCnt2 distinct positive integers, each of which is not divisible by divisor2.
    No integer is present in both arr1 and arr2.

Given divisor1, divisor2, uniqueCnt1, and uniqueCnt2, return the minimum possible maximum integer that can be present in either array.



Example 1:

Input: divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3
Output: 4
Explanation:
We can distribute the first 4 natural numbers into arr1 and arr2.
arr1 = [1] and arr2 = [2,3,4].
We can see that both arrays satisfy all the conditions.
Since the maximum value is 4, we return it.

Example 2:

Input: divisor1 = 3, divisor2 = 5, uniqueCnt1 = 2, uniqueCnt2 = 1
Output: 3
Explanation:
Here arr1 = [1,2], and arr2 = [3] satisfy all conditions.
Since the maximum value is 3, we return it.

Example 3:

Input: divisor1 = 2, divisor2 = 4, uniqueCnt1 = 8, uniqueCnt2 = 2
Output: 15
Explanation:
Here, the final possible arrays can be arr1 = [1,3,5,7,9,11,13,15], and arr2 = [2,6].
It can be shown that it is not possible to obtain a lower maximum satisfying all conditions.



Constraints:

    2 <= divisor1, divisor2 <= 105
    1 <= uniqueCnt1, uniqueCnt2 < 109
    2 <= uniqueCnt1 + uniqueCnt2 <= 109
"""
import math, sys

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l, r = 0, 2 ** 31 - 1
        small = sys.maxsize
        lcm = math.lcm(divisor1, divisor2)

        def isvalid(m):
            cnt1 = m - m // divisor1
            cnt2 = m - m // divisor2
            both_cnt = m - m // lcm

            return cnt1 >= uniqueCnt1 and cnt2 >= uniqueCnt2 and both_cnt >= (uniqueCnt1 + uniqueCnt2)

        while l <= r:
            m = (l + r) // 2
            if isvalid(m):
                small = min(small, m)
                r = m - 1
            else:
                l = m + 1

        return small


class Try1:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        arr1, arr2 = [], []
        i = 1

        # if divisor1 > divisor2 and uniqueCnt1 < uniqueCnt2:
        #     divisor1, divisor2 = divisor2, divisor1
        #     uniqueCnt1, uniqueCnt2 = uniqueCnt2, uniqueCnt1
        # if divisor1>uniqueCnt1:
        #     uniqueCnt1, uniqueCnt2 = uniqueCnt2, uniqueCnt1
        #     divisor1, divisor2 = divisor2, divisor1

        while uniqueCnt1 or uniqueCnt2:
            if i % divisor1 != 0 and uniqueCnt1:
                arr1.append(i)
                uniqueCnt1 -= 1
            elif i % divisor2 != 0 and uniqueCnt2:
                arr2.append(i)
                uniqueCnt2 -= 1
            i += 1

        print(arr1)
        print(arr2)

        return max(max(arr1), max(arr2))
