"""
https://leetcode.com/problems/unique-paths/submissions/969856783/?envType=study-plan-v2&envId=leetcode-75
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # global grid
        # NOTE: This way of assiging 2D array with outre multiply gives error
        # grid = [[0]*n]*m
        grid = [[0] * n for x in range(m)]
        if m == 1 or n == 1:
            return 1
        grid[0][1] = 1
        grid[1][0] = 1

        # for i in range(m):
        #     print(grid[i])

        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0) or (i == 0 and j == 1) or (i == 1 and j == 0):
                    continue
                # calc sum of up and left square
                # previ = i-1
                # prevj = j-1

                s = 0
                if i - 1 < 0:
                    s = grid[i][j - 1]
                elif j - 1 < 0:
                    s = grid[i - 1][j]
                else:
                    s = grid[i][j - 1] + grid[i - 1][j]

                grid[i][j] += s

        for i in range(m):
            print(grid[i])

        return grid[m - 1][n - 1]

    def uniquePaths1(self, m: int, n: int) -> int:
        global grid
        grid = [[0] * n] * m

        def traverse(i, j):
            # print(i," ",j)
            if i == m - 1 and j == n - 1:
                grid[i][j] += 1
                return

            if i > m - 1 or j > n - 1:
                return

                # down
            traverse(i + 1, j)
            # right
            traverse(i, j + 1)

        traverse(0, 0)

        for i in range(m):
            print(grid[i])

        return grid[m - 1][n - 1]