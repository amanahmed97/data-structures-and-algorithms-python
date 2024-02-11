"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest
substring
without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

"""


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1, p2 = 0, 1
        longest = 1
        if not s:
            return 0

        while p2 < len(s):
            if s[p2] not in s[p1:p2]:
                p2 += 1
            else:
                p1 += 1
            longest = max(longest, len(s[p1:p2]))

        return longest



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        m=1
        l=0
        r=1
        c=1

        while r<len(s):
            sub = s[l:r]
            if s[r] not in sub:
                c+=1
                # m = max(m,c)
                m = max(m,len(sub)+1)
                r+=1
            else:
                l+=1
                c=1
            # r+=1

        return m