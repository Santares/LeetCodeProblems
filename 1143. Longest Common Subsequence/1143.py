from functools import cache


class Solution:
    # slow
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        record = {}

        def helper(i, j):
            if (i, j) in record:
                return record[(i, j)]
            count = 0
            oi, oj = i, j
            while i < n1 and j < n2 and text1[i] == text2[j]:
                i += 1
                j += 1
                count += 1

            if i >= n1 or j >= n2:
                record[(oi, oj)] = count
                return count

            count += max(helper(i + 1, j), helper(i, j + 1))
            record[(oi, oj)] = count
            return count

        return helper(0, 0)

    # almost the same as solution1, a little bit faster
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        @cache
        def helper(i, j):
            count = 0
            while i < n1 and j < n2 and text1[i] == text2[j]:
                i += 1
                j += 1
                count += 1

            if i >= n1 or j >= n2:
                return count

            count += max(helper(i + 1, j), helper(i, j + 1))
            return count

        return helper(0, 0)

    # dp, faster
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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
