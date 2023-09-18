from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        parent = [x for x in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                parent[x] = y

        for i in range(n):
            for j in range(n):
                if i != j:
                    dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    edges.append((dis, i, j))

        edges.sort()
        res = 0
        count = 1
        for dis, i, j in edges:
            if find(i) != find(j):
                res += dis
                union(i, j)
                count += 1
                if count == n:
                    break

        return res