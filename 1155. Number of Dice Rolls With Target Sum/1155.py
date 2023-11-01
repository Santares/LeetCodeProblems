from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (target + 1) for _ in range(n)]

        for i in range(min(k, target)):
            dp[0][i + 1] = 1

        for i in range(1, n):
            for j in range(1, target + 1):
                for x in range(1, k + 1):
                    if x <= j:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % mod

        return dp[-1][-1]

    # little improved version of solution 1
    def numRollsToTarget2(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (target + 1)

        for i in range(min(k, target)):
            dp[i + 1] = 1

        for i in range(1, n):
            for j in range(target, 0, -1):
                dp[j] = 0
                for x in range(1, k + 1):
                    if x <= j:
                        dp[j] = (dp[j] + dp[j - x]) % mod

        return dp[-1]

    # Based on online solution, faster
    def numRollsToTarget3(self, n: int, k: int, target: int) -> int:
        @cache
        def helper(i, cur):
            if i == n:
                if cur == target:
                    return 1
                else:
                    return 0

            res = 0
            for j in range(1, k + 1):
                res += helper(i + 1, cur + j)
            return res % (10 ** 9 + 7)

        return helper(0, 0)

    # based on online solution, dp
    def numRollsToTarget4(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(target + 1):
                for x in range(1, k + 1):
                    if j - x >= 0:
                        dp[i][j] += dp[i - 1][j - x]

        return dp[n][target] % mod

    # Improved version of solution4
    def numRollsToTarget5(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1

        for _ in range(1, n + 1):
            for j in range(target, -1, -1):
                dp[j] = 0
                for x in range(1, k + 1):
                    if j - x >= 0:
                        dp[j] += dp[j - x]

        return dp[target] % mod
