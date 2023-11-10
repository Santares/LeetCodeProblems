from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        mons = []
        for i in range(n):
            mons.append(dist[i] / speed[i])
        mons.sort()
        t = 0
        res = 0
        while res < n:
            m = mons.pop(0)
            if m <= t:
                return res
            t += 1
            res += 1

        return res

    # Simplified version
    def eliminateMaximum2(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        mons = [dist[i] / speed[i] for i in range(n)]
        mons.sort()

        for i in range(n):
            if mons[i] <= i:
                return i

        return n