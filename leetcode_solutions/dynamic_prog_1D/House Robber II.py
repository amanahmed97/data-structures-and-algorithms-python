"""
https://leetcode.com/problems/house-robber-ii/submissions/982696840/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two
adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:

Input: nums = [1,2,3]
Output: 3

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 1000


"""

from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        def checker(num):
            n = [0] * len(num)
            if num == []:
                return 0
            if len(num) < 3:
                return max(num)

            n[0] = num[0]
            n[1] = num[1]
            n[2] = num[2] + n[0]

            for i in range(3, len(num)):
                n[i] += num[i] + max(n[i - 2], n[i - 3])

            print(n)
            return max(n)

        return max(nums[0], checker(nums[1:]), checker(nums[:-1]))

class Solution1:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
