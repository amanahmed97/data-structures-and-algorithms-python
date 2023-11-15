"""
https://leetcode.com/problems/string-compression/description/
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.



Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".



Constraints:

    1 <= chars.length <= 2000
    chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

"""

import copy
from typing import *

class Solution:
    def compress(self, chars: List[str]) -> int:
        sol = []
        ctr = 0
        current = chars[0]

        for i, c in enumerate(chars):
            if c == current and i != len(chars) - 1:
                ctr += 1
            else:
                sol.append(current)
                if i == len(chars) - 1 and c == current:
                    ctr += 1
                if ctr > 1:
                    for x in str(ctr):
                        sol.append(x)

                if i == len(chars) - 1 and c != current:
                    sol.append(c)

                current = c
                ctr = 1
        print(sol)

        i = 0
        for c in sol:
            chars[i] = c
            i += 1

        print(chars)
        remaining = len(chars) - i
        while remaining:
            chars.pop()
            remaining -= 1

        print(chars)

        return len(chars)

    def compress1(self, chars: List[str]) -> int:
        d = {}
        # sol = []

        for c in chars:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        # chars = []
        i = 0
        for c in d:
            if d[c] == 1:
                chars[i] = str(c)
                i += 1
                continue
            chars[i] = str(c)
            i += 1
            count = str(d[c])
            for x in count:
                chars[i] = str(x)
                i += 1
        remaining = len(chars) - i
        while remaining:
            chars.pop()
            remaining -= 1

        print(chars)

        return len(chars)

