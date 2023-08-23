from typing import List
from collections import defaultdict


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0

        d1 = defaultdict(int)
        d2 = defaultdict(int)
        d3 = defaultdict(int)
        d4 = defaultdict(int)

        for i, x in enumerate(nums1):
            d1[x] += 1

        for i, x in enumerate(nums2):
            d2[x] += 1

        for i, x in enumerate(nums3):
            d3[x] += 1

        for i, x in enumerate(nums4):
            d4[x] += 1

        d12 = defaultdict(int)
        d34 = defaultdict(int)

        for x in d1:
            for y in d2:
                d12[x + y] += d1[x] * d2[y]

        for x in d3:
            for y in d4:
                d34[x + y] += d3[x] * d4[y]

        for x in d12:
            if 0 - x in d34:
                res += d12[x] * d34[0 - x]

        return res
