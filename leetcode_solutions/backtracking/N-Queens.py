"""
https://leetcode.com/problems/n-queens/description/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.



Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]



Constraints:

    1 <= n <= 9
"""

from typing import *


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posD = set()
        negD = set()
        board = [["."] * n for r in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r + c) in posD or (r - c) in negD:
                    continue

                board[r][c] = "Q"
                cols.add(c)
                posD.add((r + c))
                negD.add((r - c))

                backtrack(r + 1)

                board[r][c] = "."
                cols.remove(c)
                posD.remove((r + c))
                negD.remove((r - c))

        backtrack(0)
        return res