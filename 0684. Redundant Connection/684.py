from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = {x: x for x in range(1, n + 1)}

        def find(x):
            while root[x] != x:
                x = root[x]
            return x

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                root[y] = x

        for x, y in edges:
            rx, ry = find(x), find(y)
            if rx == ry:
                return [x, y]
            else:
                union(x, y)

        return []

    # Based on online solution, dfs, slower
    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
        def dfs(node, target, visited):
            if node == target:
                return True
            for newNode in graph[node]:
                if newNode not in visited:
                    visited.add(newNode)
                    if dfs(newNode, target, visited):
                        return True
            return False

        graph = defaultdict(list)
        for x, y in edges:
            visited = set()
            if graph[x] and graph[y] and dfs(x, y, visited):
                return [x, y]
            else:
                graph[x].append(y)
                graph[y].append(x)