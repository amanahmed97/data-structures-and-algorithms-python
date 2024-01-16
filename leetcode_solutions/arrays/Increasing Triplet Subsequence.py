"""
https://leetcode.com/problems/increasing-triplet-subsequence/description

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such
that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.



Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.



Constraints:

    1 <= nums.length <= 5 * 105
    -231 <= nums[i] <= 231 - 1


Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""
import sys
from typing import *

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min = sys.maxsize
        max = sys.maxsize

        for n in nums:
            if n <= min:
                min = n
            elif n <= max:
                max = n
            else:
                return True

        return False


'''
def increasingTriplet(self, nums: List[int]) -> bool:

        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    for k in range(j+1,len(nums)):
                        if nums[j] < nums[k]:
                            return True

        return False
'''