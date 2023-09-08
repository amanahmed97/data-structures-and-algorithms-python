"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.



Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1



Constraints:

    1 <= k <= n <= 100
    1 <= times.length <= 6000
    times[i].length == 3
    1 <= ui, vi <= n
    ui != vi
    0 <= wi <= 100
    All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""

from typing import *


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        net = collections.defaultdict(list)

        for u, v, w in times:
            net[u].append((v, w))

        t = 0
        minHeap = [(0, k)]
        visit = set()

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            # t = max(t,w1)
            t = w1

            for n2, w2 in net[n1]:
                heapq.heappush(minHeap, (w1 + w2, n2))

            visit.add(n1)

        return t if len(visit) == n else -1

    def networkDelayTime1(self, times: List[List[int]], n: int, k: int) -> int:
        net = {t[0]: [] for t in times}

        for s, t, ti in times:
            net[s].append((t, ti))

        # print(net)
        visited = set()

        def dfs(s, ti):
            if s in visited:
                return 0

            for t in net.get(s, []):
                ti = ti + t[1]
                dfs(t[0], ti)

            visited.add(s)
            return ti

        op = dfs(k, 0)
        # print(visited)
        return op if len(visited) == n else -1