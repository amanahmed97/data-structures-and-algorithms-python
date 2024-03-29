"""
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two
different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one
direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of
edges changed.

It's guaranteed that each city can reach city 0 after reorder.



Example 1:

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0


"""
from typing import *
import collections


class Solution1:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(s, t) for s, t in connections}
        changes = 0
        adj = collections.defaultdict(list)
        visit = set()

        for s, t in connections:
            adj[s].append(t)
            adj[t].append(s)

        def dfs(s):
            nonlocal changes
            if s in visit:
                return
            visit.add(s)
            for t in adj[s]:
                if t not in visit:
                    if (t, s) not in edges:
                        changes += 1
                    dfs(t)

        dfs(0)
        return changes


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(s, t) for s, t in connections}
        adj = collections.defaultdict(list)  # bi directional
        minch = 0
        visit = set()

        for s, t in connections:
            # edges.add((s,t))
            adj[s].append(t)
            adj[t].append(s)

        def dfs(s):
            nonlocal minch

            for t in adj[s]:
                if t in visit:
                    continue
                if (t, s) not in edges:
                    minch += 1
                visit.add(t)
                dfs(t)

        visit.add(0)
        dfs(0)
        return minch

class Solution2:
    changes = 0
    adj = []

    def dfs(self, node, parent):
        for child in self.adj[node]:
            if child[0] != parent:
                self.changes += child[1]
                self.dfs(child[0], node)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # global changes
        # global adj
        self.adj = [[] for _ in range(n)]

        # create adjacency list
        for c in connections:
            # original edge, sign
            self.adj[c[0]].append((c[1],1))
            # artificial edge, sign
            self.adj[c[1]].append((c[0],0))

        self.dfs(0, -1)

        return self.changes