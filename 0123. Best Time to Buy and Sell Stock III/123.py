from typing import List


class Solution:
    # Online solution
    def maxProfit(self, prices: List[int]) -> int:
        last = [-prices[0], 0, -prices[0], 0]

        # for i in range(len(prices)):
        for x in prices[1:]:
            b1 = max(last[0], -x)
            s1 = max(last[1], last[0] + x)
            b2 = max(last[2], s1 - x)
            s2 = max(last[3], last[2] + x)
            last = [b1, s1, b2, s2]

        return max(last[1], last[3])
