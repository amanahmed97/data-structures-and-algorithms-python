"""
https://leetcode.com/problems/word-search/description/
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.



Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false



Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.



Follow up: Could you use search pruning to make your solution faster with a larger board?

"""

from typing import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        path = set()

        def dfs(i, j, l):
            if l == len(word):
                return True
            if i >= r or j >= c or min(i, j) < 0 or (i, j) in path or word[l] != board[i][j]:
                return False

            path.add((i, j))
            res = (dfs(i + 1, j, l + 1) or dfs(i - 1, j, l + 1) or dfs(i, j + 1, l + 1) or dfs(i, j - 1, l + 1))
            path.remove((i, j))

            return res

        for i in range(r):
            for j in range(c):
                if dfs(i, j, 0): return True

        return False