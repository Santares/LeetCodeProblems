from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def isPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True

        def helper(i, start, cur):
            if start >= n:
                res.append(list(cur))
                return

            for j in range(i, n):
                if isPalindrome(start, j):
                    word = s[start:j + 1]
                    cur.append(word)
                    helper(j + 1, j + 1, cur)
                    cur.pop()

        helper(0, 0, [])
        return res

    def partition2(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        def helper(i, start, cur):
            if start >= n:
                res.append(list(cur))
                return

            for j in range(i, n):
                word = s[start:j + 1]
                if word == word[::-1]:
                    cur.append(word)
                    helper(j + 1, j + 1, cur)
                    cur.pop()

        helper(0, 0, [])
        return res