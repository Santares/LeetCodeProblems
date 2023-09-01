from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        res = 0
        last = intervals[0]
        for x, y in intervals[1:]:
            if x >= last[1]:
                last = [x, y]
            elif y < last[1]:
                last = [x, y]
                res += 1
            else:
                res += 1

        return res

    # Based on online solution, improved version of solution 1
    def eraseOverlapIntervals2(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        last = intervals[0]
        for x, y in intervals[1:]:
            if x >= last[1]:
                last = [x, y]
            else:
                res += 1

        return res
