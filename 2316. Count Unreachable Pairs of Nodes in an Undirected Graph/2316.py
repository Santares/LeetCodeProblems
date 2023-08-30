from collections import defaultdict
from typing import List


class Solution:
    # Improved by online solution
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                parent[y] = x

        parent = {x: x for x in range(n)}

        for x, y in edges:
            union(x, y)

        res = 0
        counter = defaultdict(int)
        for i in range(n):
            counter[find(i)] += 1

        res = 0
        for cnt in counter.values():
            res += cnt * (n - cnt)

        return res // 2

    # Online solution, faster
    def countPairs2(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1] * n

        def find(x):
            while x != parent[x]:
                x = parent[x]

            return x

        def union(x, y):
            p1, p2 = find(x), find(y)

            if p1 != p2:
                if size[p1] >= size[p2]:
                    parent[p2] = p1
                    size[p1] += size[p2]
                else:
                    parent[p1] = p2
                    size[p2] += size[p1]

        for s, t in edges:
            union(s, t)

        res = 0
        for i in range(n):
            if parent[i] == i:
                res += size[i] * (n - size[i])

        return res // 2


if __name__ == '__main__':
    s = Solution()
    test1 = 7
    test2 = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
    print(s.countPairs(test1, test2))
