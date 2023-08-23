from typing import List
from collections import Counter


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = {}
        for x in nums1:
            inter[x] = 1
        for x in nums2:
            if x in inter:
                inter[x] = 2

        res = []
        for x in inter:
            if inter[x] == 2:
                res.append(x)

        return res

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = Counter(nums1) & Counter(nums2)

        return inter.keys()

    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)

        res = []
        for x in n1:
            if x in n2:
                res.append(x)

        return res

