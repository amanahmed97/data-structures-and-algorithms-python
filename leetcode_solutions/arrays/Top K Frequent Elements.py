"""
https://leetcode.com/problems/top-k-frequent-elements/description/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]



Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.



Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n = set(nums)
        n = [list() for _ in range(len(nums) + 1)]
        d = {}
        # print(n)

        for i, v in enumerate(nums):
            d[v] = 1 + d.get(v, 0)

        print(d)

        for key in d.keys():
            # print(d[k])
            n[d[key]].append(key)

        print(n)
        op = []
        c = 0
        i = len(n) - 1
        while c < k:
            if n[i]:
                # print(n[i])
                op += n[i]
                c += len(n[i])
                # print(op)
                # print(c)
            i -= 1

        return op
