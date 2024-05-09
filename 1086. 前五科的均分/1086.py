from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = defaultdict(list)
        for score in items:
            if len(students[score[0]]) == 5:
                if students[score[0]][0] < score[1]:
                    heappop(students[score[0]])
                    heappush(students[score[0]], score[1])
            else:
                heappush(students[score[0]], score[1])

        res = []
        for id, scores in students.items():
            res.append([id, sum(scores) // 5])
        res.sort()
        return res


