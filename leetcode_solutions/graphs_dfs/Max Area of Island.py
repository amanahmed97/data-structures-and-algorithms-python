"""
https://leetcode.com/problems/max-area-of-island/description/

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0



Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.
"""

from typing import *


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxa = 0
        rows = len(grid)
        columns = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r >= rows or r < 0 or c >= columns or c < 0:
                return 0
            if grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))
            a = 0
            a += dfs(r + 1, c)
            a += dfs(r - 1, c)
            a += dfs(r, c + 1)
            a += dfs(r, c - 1)

            return a + 1

        for r in range(rows):
            for c in range(columns):
                if (r, c) not in visited and grid[r][c] == 1:
                    maxa = max(dfs(r, c), maxa)

        return maxa

class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        area = 0
        visited = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or \
                    (r, c) in visited or \
                    grid[r][c] == 0:
                return 0

            directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
            visited.add((r, c))
            a = 0

            for dr, dc in directions:
                a += dfs(r + dr, c + dc)

            return 1 + a

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, dfs(r, c))

        return area

