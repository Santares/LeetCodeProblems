from collections import defaultdict
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        map = defaultdict(int)
        for x, y in paths:
            map[x] += 1
            map[y] += 0
        for key, value in map.items():
            if value == 0:
                return key