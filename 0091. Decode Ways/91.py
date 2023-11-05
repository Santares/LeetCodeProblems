class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] + [0] * len(s)

        i = 1
        while i < len(s) + 1:
            if s[i - 1] == '0':
                return 0
            elif i < len(s) and s[i] == '0':
                if s[i - 1] > '2':
                    return 0
                dp[i] = dp[i - 1]
                i += 1
                dp[i] = dp[i - 1]
            elif i > 1 and (s[i - 2] == '1' or (s[i - 2] == '2' and '0' < s[i - 1] < '7')):
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
            i += 1
        return dp[-1]

    # Based on online solution, improved version of solution1
    def numDecodings2(self, s: str) -> int:
        dp = [1] + [0] * len(s)

        for i in range(1, len(s) + 1):
            if i > 1 and (s[i - 2] == '1' or (s[i - 2] == '2' and '0' <= s[i - 1] < '7')):
                dp[i] += dp[i - 2]
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

        return dp[-1]

    # Improved version of solution 2
    def numDecodings3(self, s: str) -> int:
        a, b, c = 0, 1, 0

        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                c += b
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                c += a
            a, b, c = b, c, 0

        return b