from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        map = defaultdict(list)
        for i in range(n):
            x, y = equations[i]
            map[x].append((y, values[i]))
            map[y].append((x, 1 / values[i]))

        def bfs(a, b):
            if a == b and a in map:
                return 1
            queue = deque([(a, 1)])
            visited = {a}
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node[0] not in map:
                        continue
                    for nxt in map[node[0]]:
                        if nxt[0] not in visited:
                            visited.add(nxt[0])
                            if nxt[0] == b:
                                return node[1] * nxt[1]
                            else:
                                queue.append((nxt[0], nxt[1] * node[1]))
            return -1

        res = []
        for x, y in queries:
            res.append(bfs(x, y))

        return res
