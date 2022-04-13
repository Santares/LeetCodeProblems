from typing import List


class Solution:
    # too slow
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        def helper(rest_amount, rest_coins):
            if rest_amount == 0:
                return 0
            if len(rest_coins) == 0:
                return -1
            if rest_amount < rest_coins[0]:
                return helper(rest_amount, rest_coins[1:])
            c = rest_coins[0]
            x = rest_amount // c
            res = -1
            for i in range(x, -1, -1):
                tmp = helper(rest_amount - c * i, rest_coins[1:])
                if tmp != -1:
                    if res == -1:
                        res = tmp + i
                    else:
                        res = min(res, tmp + i)
            return res

        return helper(amount, coins)

    # online solution
    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for c in coins:
                if x >= c:
                    dp[x] = min(dp[x], 1 + dp[x - c])
        if dp[-1] == amount + 1:
            return -1
        else:
            return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    test1 =[3,7,405,436]
    test2 = 8839
    print(solution.coinChange(test1, test2))