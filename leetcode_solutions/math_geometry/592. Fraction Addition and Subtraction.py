"""
https://leetcode.com/problems/fraction-addition-and-subtraction/description/

Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.



Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"

Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"

Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"



Constraints:

    The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
    Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
    The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
    The number of given fractions will be in the range [1, 10].
    The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
"""
from typing import *
from math import *
from fractions import *


class Solution:
    def fractionAddition(self, expression: str) -> str:
        e = expression
        e = e.replace('+', ' +').replace('-', ' -').split()
        numerator = []
        denominator = []
        for t in e:
            t = t.split('/')
            numerator.append(int(t[0]))
            denominator.append(int(t[1]))
        # print(e)
        # print(numerator)
        # print(denominator)
        cm = denominator[0]
        for l in denominator:
            cm = lcm(cm, l)
        n_val = 0
        for i, n in enumerate(numerator):
            n_val += n * (cm / denominator[i])
        # print(n_val)
        cd = gcd(int(n_val), cm)
        if cd != 1:
            n_val /= cd
            cm /= cd
        return str(int(n_val)) + "/" + str(int(cm))


class Try1:
    def fractionAddition(self, expression: str) -> str:
        s = True
        n, d = 0, 1
        ans = 0.0
        nd = True

        for c in expression:
            if c == "+":
                print(n, d)
                if s:
                    ans += n / d
                else:
                    ans -= n / d
                s = True
            elif c == "-":
                print(n, d)
                if s:
                    ans += n / d
                else:
                    ans -= n / d
                s = False
            elif c.isdigit():
                if nd:
                    n = int(c)
                    nd = False
                else:
                    d = int(c)
                    nd = True
        if s:
            ans += n / d
        else:
            ans -= n / d

        # frac = ans.as_integer_ratio()
        frac = str(Fraction(ans))
        # print(frac)
        # frac = tuple(frac)
        # fracs = str(frac[0]) + "/" + str(frac([1]))

        return frac





