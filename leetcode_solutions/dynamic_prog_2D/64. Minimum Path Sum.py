"""
https://leetcode.com/problems/minimum-path-sum/description/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum
of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 200
"""
from typing import *


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid.copy()

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] += dp[i][j - 1]
                elif j == 0:
                    dp[i][j] += dp[i - 1][j]
                else:
                    dp[i][j] += min(dp[i][j - 1], dp[i - 1][j])

        return dp[len(dp) - 1][len(dp[0]) - 1]


class Solution_TLE:
    def minPathSum_DFS_TLE(self, grid: List[List[int]]) -> int:
        path = sys.maxsize
        r, c = len(grid), len(grid[0])

        def dfs(i, j, psum, visited):
            nonlocal path
            if min(i, j) < 0 or i >= r or j >= c or (i, j) in visited:
                return
            if (i, j) == (r - 1, c - 1):
                psum += grid[i][j]
                path = min(path, psum)

            visited.add((i, j))
            dfs(i + 1, j, psum + grid[i][j], visited)
            dfs(i, j + 1, psum + grid[i][j], visited)
            visited.remove((i, j))

        dfs(0, 0, 0, set())
        return path
