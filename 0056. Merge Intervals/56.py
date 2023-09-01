from typing import List


class Solution:
    # Slow
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def union(x, y):
            return [min(x[0], y[0]), max(x[1], y[1])]

        res = []
        intervals.sort(key=lambda x: x[0])

        for x, y in intervals:
            merged = False
            for i in range(len(res)):
                ox, oy = res[i]
                if oy >= x >= ox:
                    res[i] = union([x, y], [ox, oy])
                    merged = True
                    break
            if not merged:
                res.append([x, y])

        return res

    # Online solution, fast
    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if len(intervals) == 0:
            return result  # 区间集合为空直接返回

        intervals.sort(key=lambda x: x[0])  # 按照区间的左边界进行排序

        result.append(intervals[0])  # 第一个区间可以直接放入结果集中

        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:  # 发现重叠区间
                # 合并区间，只需要更新结果集最后一个区间的右边界，因为根据排序，左边界已经是最小的
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])  # 区间不重叠

        return result

    # My version of solution2
    def merge3(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for x, y in intervals[1:]:
            if x > res[-1][1]:
                res.append([x, y])
            else:
                res[-1][1] = max(y, res[-1][1])

        return res
