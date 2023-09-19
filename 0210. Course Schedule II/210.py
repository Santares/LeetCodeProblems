from collections import defaultdict, deque
from typing import List


class Solution:
    # Based on online solution, DFS
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        # 0: not visited, 1: visiting, -1, visited
        status = [0] * (numCourses + 1)
        for x, y in prerequisites:
            dic[x].append(y)

        res = []

        def dfs(i):
            if status[i] == -1:
                return True
            if status[i] == 1:
                return False

            status[i] = 1
            for j in dic[i]:
                if not dfs(j):
                    return False
            status[i] = -1
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res

    # Based on online solution, BFS
    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degrees = [0] * numCourses
        dic = defaultdict(list)

        for x, y in prerequisites:
            degrees[x] += 1
            dic[y].append(x)

        queue = deque()
        for i, d in enumerate(degrees):
            if d == 0:
                queue.append(i)

        res = []
        while queue:
            i = queue.popleft()
            res.append(i)
            for j in dic[i]:
                degrees[j] -= 1
                if degrees[j] == 0:
                    queue.append(j)

        if len(res) == numCourses:
            return res
        else:
            return []
