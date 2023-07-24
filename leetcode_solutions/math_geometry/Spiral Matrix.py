"""
https://leetcode.com/problems/spiral-matrix/submissions/

Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]



Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""

from typing import *


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        op = []
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1

        while t <= b and l <= r:
            # top row
            for i in range(l, r + 1):
                op.append(matrix[t][i])
            t += 1
            # right col
            for i in range(t, b + 1):
                op.append(matrix[i][r])
            r -= 1
            if not (l <= r and t <= b):
                break
            # bottom row
            for i in range(r, l - 1, -1):
                op.append(matrix[b][i])
            b -= 1
            # left col
            for i in range(b, t - 1, -1):
                op.append(matrix[i][l])
            l += 1

        return op