class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(n1 + 1):
            dp[i][0] = 1

        for i in range(1, n1 + 1):
            for j in range(1, min(i, n2) + 1):
                dp[i][j] += dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]

    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)

        dp = [0] * (n2 + 1)
        dp[0] = 1

        for i in range(1, n1 + 1):
            for j in range(n2, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[-1]



if __name__ == '__main__':
    s = Solution()
    test1 = "rabbbit"
    test2 = "rabbit"
    # test1 = "babgbag"
    # test2 = "bag"
    print(s.numDistinct2(test1, test2))