class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]

    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1

        first = 1
        second = 2
        for i in range(3, n + 1):
            nxt = first + second
            first, second = second, nxt

        return second