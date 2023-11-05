from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res = 0
        for x in right:
            res = max(res, n-x)
        for x in left:
            res = max(res, x-0)
        return res

    # Online solution
    def findMaximumXOR2(self, nums: List[int]) -> int:
        res = 0
        mask = 0

        for i in range(30, -1, -1):
            mask = (1 << i) | mask
            candidates = set()
            for x in nums:
                candidates.add(mask & x)
            target = res | (1 << i)
            for x in candidates:
                if x ^ target in candidates:
                    res = target
                    break

        return res
