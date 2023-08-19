from collections import defaultdict
from typing import List


class Solution:
    # Slow
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        res = 0
        visited = []
        cities = set()
        cr = defaultdict(list)

        for x, y in roads:
            cities.add(x)
            cities.add(y)
            cr[x].append((x, y))
            cr[y].append((x, y))

        cities = list(cities)

        for i in range(len(cities)):
            for j in range(i + 1, len(cities)):
                x = cities[i]
                y = cities[j]
                res = max(res, len(set(cr[x] + cr[y])))

        return res

    # Improved version of 1, faster
    def maximalNetworkRank2(self, n: int, roads: List[List[int]]) -> int:
        res = 0
        cities = defaultdict(int)
        cr = set()

        for x, y in roads:
            cities[x] += 1
            cities[y] += 1
            cr.add((x, y))

        for i in range(n):
            for j in range(i + 1, n):
                temp = cities[i] + cities[j]
                if (i, j) in cr or (j, i) in cr:
                    temp -= 1
                res = max(res, temp)

        return res


if __name__ == '__main__':
    s = Solution()
    test1 = 8
    test2 = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
    print(s.maximalNetworkRank(test1, test2))

