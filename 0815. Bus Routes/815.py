from collections import defaultdict, deque
from typing import List


class Solution:
    # slow
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        busToStop = defaultdict(set)
        stopToBus = defaultdict(list)
        visited = [False] * len(routes)
        busToBus = defaultdict(set)
        for i in range(len(routes)):
            busToStop[i] = set(routes[i])
            for s in routes[i]:
                stopToBus[s].append(i)

        for bus in busToStop:
            for s in busToStop[bus]:
                for b in stopToBus[s]:
                    if b != bus:
                        busToBus[bus].add(b)

        res = 0
        queue = deque(stopToBus[source])
        while queue:
            res += 1
            for _ in range(len(queue)):
                route = queue.popleft()
                if target in busToStop[route]:
                    return res
                else:
                    for b in busToBus[route]:
                        if not visited[b]:
                            visited[b] = True
                            queue.append(b)

        return -1
