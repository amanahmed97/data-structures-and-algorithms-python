"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]



Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
"""

from typing import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i, n in enumerate(nums):
            if n != 0:
                nums[p] = n
                p += 1

        while p < len(nums):
            nums[p] = 0
            p += 1


'''
sol = []
        ctr=0
        for n in nums:
            if n == 0:
                ctr+=1
                continue
            sol.append(n)

        while ctr>0:
            sol.append(0)

        nums = sol
'''