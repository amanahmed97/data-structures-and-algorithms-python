"""
https://leetcode.com/problems/merge-intervals/description/
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.



Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104


"""

from typing import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            currEnd = res[-1][1]
            if start <= currEnd:
                res[-1][1] = max(currEnd, end)
            else:
                res.append([start, end])

        return res

    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 1
        if len(intervals) < 2:
            return intervals

        # for i in range(1,len(intervals)):
        while i < len(intervals):
            if intervals[i - 1][1] < intervals[i][0]:
                res.append(intervals[i - 1])
                res.append(intervals[i])
                i += 1
            elif intervals[i - 1][1] >= intervals[i][0]:
                res.append([min(intervals[i - 1][0], intervals[i][0]),
                            max(intervals[i - 1][1], intervals[i][1])])
                i += 1
            # else:
            #     res.append(intervals[i])
            i += 1

        return res

