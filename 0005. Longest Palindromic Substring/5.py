class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        maxRes = 1
        res = s[0]

        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if i + 1 == j:
                        dp[i][j] = 1
                        nr = j - i + 1
                    else:
                        nxt = i + 1
                        if dp[nxt][j - 1] == 1:
                            dp[i][j] = 1
                            nr = j - i + 1
                        else:
                            nr = 0
                    if nr > maxRes:
                        maxRes = nr
                        res = s[i:i + nr]

        return res

    # Based on online solution
    def longestPalindrome2(self, s: str) -> str:
        n = len(s)

        def helper(i, j):
            while 0 <= i and j < n:
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    break
            return j - i - 1

        res = s[0]
        maxR = 1

        for i in range(n - 1):
            r = helper(i, i)
            if r > maxR:
                maxR = r
                start = i - r // 2
                res = s[start:start + r]

            r = helper(i, i + 1)
            if r > maxR:
                maxR = r
                start = i - r // 2 + 1
                res = s[start:start + r]

        return res

    # Based on online solution
    def longestPalindrome3(self, s: str) -> str:
        def helper(l,r):
            while l-1 >= 0 and r+1 <n:
                if s[l-1] != s[r+1]:
                    return l, r
                l -=1
                r += 1
            return l, r

        res = s[0]
        n = len(s)
        for i in range(n-1):
            l, r = helper(i, i)
            if r-l+1 > len(res):
                res = s[l:r+1]
            if s[i] == s[i+1]:
                l, r = helper(i, i+1)
                if r-l+1 > len(res):
                    res = s[l:r+1]

        return res

if __name__ == '__main__':
    s = Solution()
    test = "babad"
    test = "cbbd"
    # test = "ccc"
    test = "adam"
    print(s.longestPalindrome3(test))
