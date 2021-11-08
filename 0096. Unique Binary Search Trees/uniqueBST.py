from functools import cache
from math import factorial


class Solution:
    # brutal force, very slow
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1

        n = n - 1

        ans = 0
        for i in range(n // 2 + n % 2):
            ans += (self.numTrees(n - i) * self.numTrees(i)) * 2
        if n % 2 == 0:
            ans += self.numTrees(n // 2) * self.numTrees(n // 2)

        return ans

    # dp, faster
    def numTrees2(self, n: int) -> int:
        self.dic = {1: 1, 0: 1}

        def helper(n):
            if n not in self.dic:
                ans = 0
                for i in range(n):
                    ans += helper(n - i - 1) * helper(i)
                self.dic[n] = ans
            return self.dic[n]

        return helper(n)

    # improved version of 1, not faster than 2
    def numTrees3(self, n: int) -> int:
        self.dic = {1: 1, 0: 1}

        def helper(n):
            if n not in self.dic:
                ans = 0
                n = n - 1

                for i in range(n // 2 + n % 2):
                    ans += (helper(n - i) * helper(i)) * 2
                if n % 2 == 0:
                    ans += helper(n // 2) * helper(n // 2)

                self.dic[n+1] = ans
                return ans
            return self.dic[n]

        return helper(n)

    # online solution, dp, faster
    @cache
    def numTrees4(self, n: int) -> int:
        if n <= 1: return 1
        return sum(self.numTrees(i-1) * self.numTrees(n-i) for i in range(1, n+1))

    # online solution, fast
    def numTrees5(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]

    # online solution, math (Catalan Numbers), not so fast
    def numTrees6(self, n: int) -> int:
        return factorial(2*n) // (factorial(n)*factorial(n+1))


if __name__ == '__main__':
    solution = Solution()
    print(solution.numTrees3(3))
