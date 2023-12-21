from collections import defaultdict
from typing import List


class Solution:
    # slow, but acceptable
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                count = 2
                for k in range(j+1, n):
                    x3, y3 = points[k]
                    # x1-x2/y1-y2 == x2-x3/y2-y3
                    # (x1-x2) * (y2-y3) == (x2-x3)*(y1-y2)
                    if (x1-x2) * (y2-y3) == (x2-x3)*(y1-y2):
                        count += 1
                res = max(res, count)

        return res

    # based on online solution, much faster
    def maxPoints2(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        res = 1
        n = len(points)
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            count = 0
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x1 - x2
                dy = y1 - y2
                k = gcd(dx, dy)
                slopes[(dx // k, dy // k)] += 1
                count = max(count, slopes[(dx // k, dy // k)])
            res = max(res, count + 1)

        return res
