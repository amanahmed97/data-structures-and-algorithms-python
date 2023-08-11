"""
https://leetcode.com/problems/encode-and-decode-strings/
https://www.lintcode.com/problem/659/

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Only $39.9 for the "Twitter Comment System Project Practice" within a limited time of 7 days!

WeChat Notes Twitter for more information（WeChat ID jiuzhang104）
Example

Example1

Input: ["lint","code","love","you"]

Output: ["lint","code","love","you"]

Explanation:

One possible encode method is: "lint:;code:;love:;you"

Example2

Input: ["we", "say", ":", "yes"]

Output: ["we", "say", ":", "yes"]

"""

from typing import *


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        code = ""
        for s in strs:
            code += str(len(s))
            code += "#"
            code += s

        self.decode(code)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        res = []
        print(str)
        i = 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[j - 1])
            res.append(str[j + 1:j + length + 1])
            i = j + length + 1

        print(res)
        return res


s = Solution()
s.encode(["abc", "defs", "chea", "a", "asc"])