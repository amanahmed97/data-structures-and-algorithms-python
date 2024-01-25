"""
https://leetcode.com/problems/permutations/
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]



Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
"""

from typing import *


class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        op = []

        def backtrack(subset, visit):
            if len(subset) == len(nums):
                op.append(subset[:])
                return

            for n in nums:
                if n not in visit:
                    visit.add(n)
                    subset.append(n)
                    backtrack(subset, visit)
                    visit.remove(n)
                    subset.pop()

        backtrack([], set())
        return op


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        subset = []

        self.backtrack(nums, visited, subset, res)
        return res

    def backtrack(self, nums, visited, subset, res):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtrack(nums, visited, subset + [nums[i]], res)
                visited.remove(i)

    def permuteNC(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            res.extend(perms)
            nums.append(n)

        return res
