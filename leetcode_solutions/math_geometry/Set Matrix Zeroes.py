"""
https://leetcode.com/problems/set-matrix-zeroes/description/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.



Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]



Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1



Follow up:

    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
"""

from typing import *


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        # rm = [False]*r
        # cm = [False]*c
        rm = []
        cm = []

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    # rm[r] = True
                    # cm[c] = True
                    rm.append(i)
                    cm.append(j)

        for rz in rm:
            for j in range(c):
                matrix[rz][j] = 0

        for cz in cm:
            for i in range(r):
                matrix[i][cz] = 0

