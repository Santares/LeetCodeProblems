from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        inserted = False
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals = intervals[:i] + [newInterval] + intervals[i:]
                inserted = True
                break
        if not inserted:
            intervals.append(newInterval)

        last = [-1, -1]
        res = []
        for s, e in intervals:
            if s <= last[1]:
                last[1] = max(last[1], e)
                res[-1][1] = last[1]
            else:
                last = [s, e]
                res.append([s, e])

        return res



if __name__ == '__main__':
    s = Solution()
    # test1 = [[1,3],[6,9]]
    # test2 = [2,5]
    # test1 = []
    # test2 = [5,7]
    test1 = [[1,5]]
    # test2 = [6,8]
    test2 = [0,3]
    print(s.insert(test1, test2))