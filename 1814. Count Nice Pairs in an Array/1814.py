from collections import defaultdict
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # A + rev(b) = rev(a) + b
        # a - rev(a) = b - rev(b)
        values = defaultdict(int)
        for x in nums:
            revX = int(str(x)[::-1])
            values[x - revX] += 1

        res = 0
        for k, v in values.items():
            if v > 1:
                res += v * (v - 1) // 2

        return res % (10 ** 9 + 7)
