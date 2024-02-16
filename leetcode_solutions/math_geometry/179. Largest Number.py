"""
https://leetcode.com/problems/largest-number/description/

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"



Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 109
"""
from functools import cmp_to_key
from typing import *
from collections import *


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numd = defaultdict(list)
        op = ""

        def compare(x, y):
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        for n in nums:
            ns = str(n)
            numd[int(ns[0])].append(str(n))

        for n in range(9, -1, -1):
            numd[n].sort(key=cmp_to_key(compare), reverse=True)
            for v in numd[n]:
                op += v

        return op.lstrip('0') or '0'
