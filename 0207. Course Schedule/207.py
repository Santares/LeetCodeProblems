from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        passed = set()
        for x, y in prerequisites:
            dic[x].append(y)

        def helper(x, visited):
            if x in passed:
                return True
            for y in dic[x]:
                if y in visited:
                    return False
                else:
                    visited.add(y)
                    if not helper(y, visited):
                        return False
                    visited.remove(y)
            return True

        for i in range(1, numCourses + 1):
            visited = {i}
            if not helper(i, visited):
                return False
            passed.add(i)

        return True

    # Based on online solution
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        # 0: not visited, 1: visited, -1, passed
        status = [0] * (numCourses + 1)
        for x, y in prerequisites:
            dic[x].append(y)

        def helper(x):
            if status[x] == -1:
                return True
            if status[x] == 1:
                return False

            status[x] = 1

            for y in dic[x]:
                if not helper(y):
                    return False

            status[x] = -1
            return True

        for i in range(1, numCourses + 1):
            if not helper(i):
                return False

        return True