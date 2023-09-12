from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        table = defaultdict(list)
        for i, x in enumerate(groupSizes):
            if len(table[x]) == 0 or len(table[x][-1]) == x:
                table[x].append([i])
            else:
                table[x][-1].append(i)

        res = []
        for group in table.values():
            res += group

        return res
