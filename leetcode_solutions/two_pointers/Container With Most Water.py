"""
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
"""
from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp = 0
        rp = len(height) - 1
        max = min(height[lp], height[rp]) * (rp - lp)

        # if len ==2

        i = 0
        while lp <= len(height) - 1 and rp > 0:
            c = min(height[lp], height[rp]) * (rp - lp)

            if c > max:
                max = c

            if height[lp] > height[rp]:
                rp -= 1
                # print("lp:",lp," rp:",rp," max:",max)
            elif height[rp] > height[lp]:
                lp += 1
                # print("lp:",lp," rp:",rp," max:",max)
            else:
                lp += 1

            i += 1

        print("lp:", lp, " rp:", rp, " max:", max)
        return max