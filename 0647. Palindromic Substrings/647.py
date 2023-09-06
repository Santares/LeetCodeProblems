class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = n
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n):
        # for i in range(n + 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j]:
                        res += 1
                else:
                    continue

        return res

    def countSubstrings2(self, s: str) -> int:
        n = len(s)
        res = 0

        def helper(l, r):
            count = 0
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    return count
            return count

        for i in range(n):
            if i > 0:
                res += helper(i - 1, i)
            res += helper(i, i)

        return res


if __name__ == '__main__':
    s = Solution()
    test = "abba"
    # test = "aaa"
    print(s.countSubstrings(test))