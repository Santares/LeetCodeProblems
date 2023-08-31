from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) <= 1:
        #     return 0

        totalProfit = 0

        buy = prices[0]
        sell = prices[0]

        for x in prices:
            if x > sell:
                sell = x
            else:
                totalProfit += sell - buy
                buy = x
                sell = x

        totalProfit += sell - buy

        return totalProfit

    # online solution
    def maxProfit2(self, prices: List[int]) -> int:
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxProfit += prices[i] - prices[i - 1]

        return maxProfit

    # 2023/08/30
    def maxProfit3(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        for x in prices[1:]:
            if x > buy:
                res += x - buy
            buy = x

        return res