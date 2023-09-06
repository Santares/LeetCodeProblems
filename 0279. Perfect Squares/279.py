import math


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for x in range(1, n+1):
            j = math.sqrt(x)
            if int(j) == j:
                dp[x] = 1
            else:
                j = int(j)
                for i in range(1, j+1):
                    dp[x] = min(dp[x], dp[x-i*i]+1)

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    test = 12
    print(s.numSquares(test))