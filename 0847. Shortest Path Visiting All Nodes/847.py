from typing import List


class Solution:
    # Based on online solution
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        queue = deque((i, 1 << i, 0) for i in range(n))
        visited = {(i, 1 << i) for i in range(n)}

        while queue:
            for _ in range(len(queue)):
                node, status, distance = queue.popleft()
                for nxt in graph[node]:
                    newStatus = status | 1 << nxt
                    if (nxt, newStatus) not in visited:
                        if newStatus == (1 << n) - 1:
                            return distance + 1
                        queue.append((nxt, newStatus, distance + 1))
                        visited.add((nxt, newStatus))

        return 0