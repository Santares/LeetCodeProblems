from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[1])
        last = points[0]
        res = 1
        for x,y in points[1:]:
            if x > last[1]:
                res += 1
                last = [x,y]

        return res

    def findMinArrowShots2(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        last = points[0]
        res = 1
        for x, y in points[1:]:
            if x > last[1]:
                res += 1
                last = [x, y]
            else:
                last[1] = min(y, last[1])

        return res