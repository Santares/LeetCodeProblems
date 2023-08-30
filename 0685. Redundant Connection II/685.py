from collections import defaultdict
from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        def find(x):
            while root[x] != x:
                x = root[x]
            return x

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                root[y] = x

        inDegree = defaultdict(int)
        candidateY = -1
        candidateX = -1
        for x, y in edges:
            inDegree[y] += 1
            if inDegree[y] == 2:
                candidateY = y
                candidateX = x

        # check
        root = {x: x for x in range(1, n + 1)}
        res = []
        for x, y in edges:
            if x == candidateX and y == candidateY:
                continue
            rx, ry = find(x), find(y)
            if rx == ry:
                res = [x, y]
            else:
                union(x, y)

        if res == []:
            return [candidateX, candidateY]
        else:
            if candidateX == -1:
                return res
            else:
                for x, y in edges:
                    if x != candidateX and y == candidateY:
                        return [x, y]


if __name__ == '__main__':
    s = Solution()
    test = [[2, 1], [3, 1], [4, 2], [1, 4]]
    # test = [[4,2],[1,5],[5,2],[5,3],[2,4]]
    test = [[1, 2], [1, 3], [2, 3]]
    print(s.findRedundantDirectedConnection(test))
