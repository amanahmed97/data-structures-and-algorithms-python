"""
https://leetcode.com/problems/meeting-rooms/
https://www.lintcode.com/problem/920/

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Only $39.9 for the "Twitter Comment System Project Practice" within a limited time of 7 days!

WeChat Notes Twitter for more information（WeChat ID jiuzhang104）

(0,8),(8,10) is not conflict at 8
Example

Example1

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false

Explanation:

(0,30), (5,10) and (0,30),(15,20) will conflict

Example2

Input: intervals = [(5,8),(9,15)]

Output: true

Explanation:

Two times will not conflict
"""

# Solution TBD

from typing import (
    List,
)


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        f, l = intervals[0][0], intervals[0][1]
        intervals.sort()

        for s, e in intervals:
            if s > f and e < l:
                return False
            if s > l:
                l = e

        return True


s = Solution()
"""
[(0,30),(5,10),(15,20)]
[(5,8),(9,15)]
"""
ans = s.can_attend_meetings([(5, 8), (9, 15)])

print(ans)