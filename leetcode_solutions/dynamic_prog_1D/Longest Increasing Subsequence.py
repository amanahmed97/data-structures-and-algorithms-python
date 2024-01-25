"""
https://leetcode.com/problems/longest-increasing-subsequence/description/
Given an integer array nums, return the length of the longest strictly increasing
subsequence

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:

    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

"""
from typing import *


class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if dp[j] < dp[i]:
                    continue
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class Try1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        res = 0

        for n in nums:
            if not sub:
                sub.append(n)
            elif n <= sub[-1]:
                sub.pop()
                # sub.append(n)
            # else:
            sub.append(n)

            res = max(res, len(sub))

        return res - 1
