from typing import List

class Solution:
    # too slow
    def maxProfit(self, prices: List[int]) -> int:
        record = []

        for x in prices:
            for i in range(len(record)):
                record[i][1] = max(record[i][1], x)

            record.append([x, x])

        profit = 0
        for p in record:
            profit = max(p[1] - p[0], profit)

        return profit

    # too slow
    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            newProfit = max(prices[i:]) - prices[i]
            profit = max(profit, newProfit)

        return profit

    # faster
    def maxProfit3(self, prices: List[int]) -> int:
        profit = 0

        minPrice = prices[0]

        for x in prices:
            profit = max(profit, x - minPrice)
            minPrice = min(minPrice, x)

        return profit

    # very fast
    def maxProfit4(self, prices: List[int]) -> int:
        profit = 0

        minPrice = prices[0]
        sell = prices[0]

        for x in prices:
            if x < minPrice:
                minPrice = x
                sell = x
            if x > sell:
                profit = max(profit, x - minPrice)
                sell = x

        return profit

    # 2023/08/30
    def maxProfit5(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0
        for x in prices[1:]:
            if x < buy:
                buy = x
            else:
                res = max(res, x - buy)

        return res

    # 2023/08/30
    def maxProfit6(self, prices: List[int]) -> int:
        dp = [x for x in prices]

        res = 0
        for i in range(1, len(prices)):
            dp[i] = min(dp[i - 1], prices[i])
            res = max(res, prices[i] - dp[i])
        return res


if __name__ == '__main__':
    solution = Solution()
    test = [1,4,1,4,3,1]
    print(solution.maxProfit3(test))
