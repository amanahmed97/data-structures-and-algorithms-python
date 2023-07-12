"""
https://leetcode.com/problems/maximum-product-subarray/description/
Given an integer array nums, find a
subarray
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.



Constraints:

    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxv,minv = 1,1
        res = nums[0]

        for n in nums:
            tmp = maxv*n
            maxv = max(maxv*n,minv*n,n)
            minv = min(tmp,minv*n,n)
            res = max(res,maxv)

        return res

    def maxProduct2(self, nums: List[int]) -> int:
        n = [1]*len(nums)
        if len(nums)<2:
            return nums[0]
        if len(nums)<3:
            return max(nums[0],nums[1],nums[0]*nums[1])
        n[0] = nums[0]

        for i in range(1,len(nums)):
            n[i] *= nums[i] * n[i-1]
        print(n)
        return max(n+nums)

    def maxProduct1(self, nums: List[int]) -> int:
        n = [1]*len(nums)

        n[0] = nums[0]

        for i in range(1,len(nums)):
            if (nums[i]>0 and n[i-1]>0) or (nums[i]<0 and n[i-1]<0):
                n[i] *= nums[i] * n[i-1]
            else:
                n[i] *= nums[i]
        print(n)
        return max(n)