from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3
        res = 0
        j = 1
        for i in range(n):
            res += piles[j]
            j += 2

        return res