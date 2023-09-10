"""
https://leetcode.com/problems/combination-sum-ii/description/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]



Constraints:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30
"""

from typing import *


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(pos, subset, target):
            if target == 0:
                res.append(subset[::])
                return
            if target < 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue

                subset.append(candidates[i])
                backtrack(i + 1, subset, target - candidates[i])
                subset.pop()
                prev = candidates[i]

        backtrack(0, [], target)
        return res

    def combinationSum2t1(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, subset):
            if sum(subset) == target:
                res.append(subset[::])
                return
            if i == len(candidates):
                return

            subset.append(candidates[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(candidates) and sum(subset) + candidates[i] <= target:
                i += 1

            backtrack(i + 1, subset)

        backtrack(0, [])
        return res