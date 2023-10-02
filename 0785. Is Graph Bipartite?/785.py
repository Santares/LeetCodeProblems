from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)

        def dfs(node, flag):
            if color[node] == flag * -1:
                return False
            elif color[node] == flag:
                return True

            color[node] = flag
            for nxt in graph[node]:
                res = dfs(nxt, flag * -1)
                if not res:
                    return False

            return True

        for node in range(len(graph)):
            if color[node] == 0:
                res = dfs(node, 1)
                if not res:
                    return False
        return True

    def isBipartite2(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)

        def bfs(node, flag):
            queue = deque([node])
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if color[node] == flag * -1:
                        return False
                    color[node] = flag
                    for nxt in graph[node]:
                        if color[nxt] == 0:
                            queue.append(nxt)
                flag *= -1

            return True

        for node in range(len(graph)):
            if color[node] == 0:
                res = bfs(node, 1)
                if not res:
                    return False
        return True