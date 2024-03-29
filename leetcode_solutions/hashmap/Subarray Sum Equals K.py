"""
https://leetcode.com/problems/subarray-sum-equals-k/description/

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Constraints:

    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000
    -107 <= k <= 107
"""

"""
Prefix Sum Concept
"""

from typing import *

# O(n) Time complexity
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psum = {0: 1}
        count = 0
        sum = 0

        for n in nums:
            sum += n
            diff = sum - k
            if diff in psum.keys():
                count += psum[diff]
            psum[sum] = 1 + psum.get(sum, 0)

        return count
