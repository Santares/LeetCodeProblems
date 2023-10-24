from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for key in count:
            x = count[key]
            if x > 1:
                res += (x - 1) * x // 2
        return res

    # Based on online solution, faster
    def numIdenticalPairs2(self, nums: List[int]) -> int:
        count = {}
        res = 0
        for x in nums:
            if x not in count:
                count[x] = 0
            else:
                count[x] += 1
                res += count[x]
        return res
