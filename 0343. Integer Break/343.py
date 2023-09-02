class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]* (n+1)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n+1):
            res = 0
            for j in range(2, i):
                res = max((i-j)*dp[j], res, (i-j)*j)
            dp[i] = res

        return dp[-1]