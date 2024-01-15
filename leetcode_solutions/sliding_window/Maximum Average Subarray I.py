"""
https://leetcode.com/problems/maximum-average-subarray-i/description/

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000



Constraints:

    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104


"""

from typing import *
import sys

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sliding window
        l = 0;
        r = l + k - 1
        maxa = -sys.maxsize

        if len(nums) == 1:
            return nums[0]

        subsum = sum(nums[l:(r)])

        while r <= len(nums) - 1:
            # sub = nums[l:r]
            # avg = sum(sub)/k
            subsum += nums[r]

            avg = subsum / k

            if avg > maxa:
                maxa = avg

            subsum -= nums[l]
            # subsum += nums[r+1]
            l += 1
            r += 1

        return maxa

    def findMaxAverage1(self, nums: List[int], k: int) -> float:
        # sliding window
        l = 0;
        r = l + k
        maxa = -sys.maxsize

        if len(nums) == 1:
            return nums[0]

        while r <= len(nums):
            sub = nums[l:r]
            avg = sum(sub) / k

            if avg > maxa:
                maxa = avg

            l += 1
            r += 1

        return maxa