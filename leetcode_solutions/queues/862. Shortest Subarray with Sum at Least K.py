"""
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/?source=submission-noac

Refer:
https://leetcode.com/problems/minimum-size-subarray-sum/description/
https://leetcode.com/problems/subarray-sum-equals-k/description/

Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1], k = 1
Output: 1

Example 2:

Input: nums = [1,2], k = 4
Output: -1

Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3



Constraints:

    1 <= nums.length <= 105
    -105 <= nums[i] <= 105
    1 <= k <= 109
"""

from typing import *
import sys

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        psum = [0]
        res = len(nums) + 1
        sum = 0
        monoq = []

        for n in nums:
            sum += n
            psum.append(sum)

        sum = 0
        for i, v in enumerate(psum):
            while monoq and v <= psum[monoq[-1]]:
                monoq.pop()
            while monoq and v - psum[monoq[0]] >= k:
                res = min(res, i - monoq.pop(0))
            monoq.append(i)

        return res if res < len(nums) + 1 else -1

# Brute Force
class Solution_BF_TLE:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = sys.maxsize
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum+=nums[j]
                if sum>=k:
                    res = min(res, j-i+1)

        return res if res<sys.maxsize else -1
