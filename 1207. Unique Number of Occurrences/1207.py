from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        if len(set(arr)) != len(set(count.values())):
            return False
        return True