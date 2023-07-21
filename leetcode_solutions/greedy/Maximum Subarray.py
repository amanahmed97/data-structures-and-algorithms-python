"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the
subarray
with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.



Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104



Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""
from typing import  *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0

        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res

    def maxSubArray1(self, nums: List[int]) -> int:
        large = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            s = sum(nums[l:(r + 1)])
            if s > large:
                large = s

            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1

        return large