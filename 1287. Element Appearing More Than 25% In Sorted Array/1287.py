import bisect
from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr) / 4
        count = Counter(arr)
        for key, value in count.items():
            if value > n:
                return key
        return 0

    # online solution, binary search, faster
    def findSpecialInteger2(self, arr: List[int]) -> int:
        n = len(arr) // 4
        i = 0
        while i < len(arr):
            x = arr[i]
            l = bisect.bisect_left(arr, x)
            r = bisect.bisect_right(arr, x)
            if r - l > n:
                return x

            i += n