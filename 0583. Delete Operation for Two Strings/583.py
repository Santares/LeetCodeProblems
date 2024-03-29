class Solution:
    # Used 1143's solution
    def minDistance(self, word1: str, word2: str) -> int:
        def helper(text1, text2):
            n1 = len(text1)
            n2 = len(text2)
            dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

            for i in range(1, n1 + 1):
                for j in range(1, n2 + 1):
                    if text1[i - 1] == text2[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            return dp[-1][-1]

        return len(word1) + len(word2) - 2 * helper(word1, word2)

    def minDistance2(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            dp[i][0] = i

        for j in range(1, n2 + 1):
            dp[0][j] = j

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]
