"""

"""
from typing import *

class Solution:
    def countBits(self, n: int) -> List[int]:
        def onebits(i: int):
            b = 0
            ctr = 0
            while i > 0:
                r = i % 2
                # print(r)
                if r:
                    ctr += 1
                b = b*10 + r
                i = i // 2
            print(b)

            return ctr
                # sum(list(b))

        op = [0] * (n + 1)

        for i, v in enumerate(op):
            op[i] = onebits(i)

        return op

s = Solution()
a = s.countBits(7)
print(a)