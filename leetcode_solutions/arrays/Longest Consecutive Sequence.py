"""
https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9



Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
"""

from typing import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in ns:
                l = 0
                while n in ns:
                    l += 1
                    n = n + 1
                longest = max(l, longest)

        return longest

    def longestConsecutiveTLE(self, nums: List[int]) -> int:
        ns = set(nums)
        longest = 1

        for n in nums:
            # if (n-1) in ns:
            l = 0
            while n in ns:
                l += 1
                n = n - 1
            longest = max(l, longest)

        return longest if nums else 0

    def longestConsecutive1(self, nums: List[int]) -> int:
        nums.sort()
        nums = [*set(nums)]
        if not nums:
            return 0

        longest = 0
        prev = nums[0]
        l = 1
        for i in range(1, len(nums)):
            if nums[i] == prev + 1:
                # print(l)
                # print(nums[i])
                l += 1
                print('l', l)
            else:
                longest = max(l, longest)
                # print('long',longest)
                l = 1
            prev = nums[i]
            print(prev)
        longest = max(l, longest)

        return longest