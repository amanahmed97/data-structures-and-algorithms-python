"""
https://leetcode.com/problems/number-of-islands/description/
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
 all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3



Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.


"""

from typing import *


class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visit = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if (r, c) in visit or min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(r, c):
            if (r, c) in visited or r >= row or c >= col or min(r, c) < 0:
                # visited.remove((r,c))
                return False
            if grid[r][c] == "0":
                # visited.remove((r,c))
                return False

            if grid[r][c] == "1":
                visited.add((r, c))
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

            return True

        for i in range(row):
            for j in range(col):
                if (i, j) not in visited and grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        print(visited)
        return count
