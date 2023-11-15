"""
https://leetcode.com/problems/decode-string/description/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"



Constraints:

    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].


"""

from typing import *


class Solution:
    def decodeString(self, s: str) -> str:
        stack = [];
        curNum = 0;
        curStr = "";

        for c in s:
            if c == '[':
                stack.append(curStr)
                stack.append(curNum)
                curNum = 0
                curStr = ""
            elif c == ']':
                num = stack.pop()
                prevStr = stack.pop()
                curStr = prevStr + int(num) * curStr
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curStr += c

        return curStr

    def decodeString1(self, s: str) -> str:
        stack = []
        sol = ""
        octr = 0

        for c in s:
            if c == '[':
                octr += 1
            if c != ']':
                stack.append(c)
            elif octr > 0:
                # sc = stack.pop()
                # ss = sc + ""
                sc, ss = "", ""

                # if open == True:
                while sc != '[':
                    ss = sc + ss
                    sc = stack.pop()
                octr -= 1

                num = stack.pop()
                if type(int(num)) == int:
                    sol = sol + int(num) * ss
                else:
                    # ss = num + ss
                    sol = sol + ss

        sc, ss = "", ""
        print(sol)
        while octr != 0:
            sc, ss = "", ""
            while sc != '[':
                ss = sc + ss
                sc = stack.pop()
            octr -= 1

            num = stack.pop()
            if type(int(num)) == int:
                sol = sol + int(num) * ss
            else:
                ss = ss + num
                sol = sol + ss

        ss = ""
        while len(stack) != 0:
            ss = stack.pop() + ss
        sol = sol + ss

        return sol

    def decodeString2(s: str) -> str:
        stack = []
        sol = ""
        octr = 0

        for i, c in enumerate(s):
            if c == '[':
                octr += 1
            if c != ']':
                stack.append(c)
            elif octr > 0:
                sc, ss = "", ""

                # if open == True:
                while sc != '[':
                    ss = sc + ss
                    sc = stack.pop()
                octr -= 1

                num = stack.pop()
                if type(int(num)) == int:
                    if octr > 0:
                        print("1octr ", octr)
                        sol = sol + int(num) * ss
                    elif octr == 0 and i < len(s):
                        print("2octr ", octr)
                        sol = int(num) * (ss + sol)
                    else:
                        sol = sol + int(num) * ss
                else:
                    # ss = num + ss
                    sol = sol + ss
