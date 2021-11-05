from functools import lru_cache
import math


class Solution:
    # math, fast
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))

    # math
    def uniquePaths2(self, m: int, n: int) -> int:
        return math.comb(m+n-2, m-1)


    @lru_cache
    def uniquePaths3(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    # dynamic programing
    def uniquePaths4(self, m: int, n: int) -> int:
        dp = [[1] * n]
        row = [1] + [0] * (n - 1)
        for i in range(m - 1):
            dp.append(row)

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

    # online solution
    def uniquePaths5(self, m: int, n: int) -> int:
        dp = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[n - 1]



