"""
https://leetcode.com/problems/number-of-provinces/description/?envType=study-plan-v2&envId=leetcode-75

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3



Constraints:

    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]


"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # visited = [False]*len(isConnected)
        visited = []
        count = 0

        def route(p, visited):
            visited.append(p)
            for i, r in enumerate(isConnected[p]):
                if r == 1 and i not in visited:
                    route(i, visited)

        # print(isConnected[0])
        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                route(i, visited)

        print(visited)

        return count

    def findCircleNum1(self, isConnected: List[List[int]]) -> int:
        provinces = []

        def route(p, province):
            for i, r in enumerate(isConnected[p]):
                add = 0
                if r == 1:
                    if i not in province:
                        province.append(i)
                        add += 1
            if add > 0:
                for i in province:
                    route(i, province)

            return province

        # print(isConnected[0])
        for i in range(len(isConnected)):
            province = (route(i, []))
            add = True
            for p in provinces:
                if province[0] in p:
                    add = False
                    break
            if add:
                provinces.append(province)

        print(provinces)
        provinces = set(map(tuple, provinces))
        return len(provinces)
