from typing import List


class Solution:
    # Online solution
    # d[i][j][k] means the number of ways of using exactly j people, in first i jobs, minProfit = k
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        n2 = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(n2 + 1)]
        mod = 10 ** 9 + 7

        for j in range(n + 1):
            dp[0][j][0] = 1

        for i in range(1, n2 + 1):
            for j in range(1, n + 1):
                for k in range(minProfit + 1):
                    if j >= group[i - 1]:
                        dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - group[i - 1]][max(0, k - profit[i - 1])]
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        res = dp[-1][-1][-1]

        return res % mod

    # d[i][j][k] means the number of ways of using ast most j people, in first i jobs, minProfit = k
    def profitableSchemes2(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        n2 = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(n2 + 1)]
        mod = 10 ** 9 + 7

        for j in range(n + 1):
            dp[0][j][0] = 1

        for i in range(1, n2 + 1):
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j >= group[i - 1]:
                        dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - group[i - 1]][max(0, k - profit[i - 1])]
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        res = dp[-1][-1][-1]

        return res % mod

    # Improved version of solution 3
    def profitableSchemes3(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        n2 = len(group)
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        mod = 10 ** 9 + 7

        for j in range(n + 1):
            dp[j][0] = 1

        for i in range(1, n2 + 1):
            for j in range(n, group[i - 1] - 1, -1):
                for k in range(minProfit + 1):
                    if j >= group[i - 1]:
                        dp[j][k] = (dp[j][k] + dp[j - group[i - 1]][max(0, k - profit[i - 1])])

        res = dp[-1][-1]

        return res % mod

    # Improved version of solution 1
    def profitableSchemes4(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        n2 = len(group)
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        mod = 10 ** 9 + 7

        dp[0][0] = 1

        for i in range(1, n2 + 1):
            for j in range(n, -1, -1):
                for k in range(minProfit + 1):
                    if j >= group[i - 1]:
                        dp[j][k] = dp[j][k] + dp[j - group[i - 1]][max(0, k - profit[i - 1])]

        res = sum([dp[j][-1] for j in range(n + 1)])

        return res % mod


if __name__ == '__main__':
    s = Solution()
    test1 = 5
    test2 = 3
    test3 = [2,2]
    test4 = [3,2]

    test1 = 1
    test2 = 1
    test3 = [1,1,1,1,2,2,1,2,1,1]
    test4 = [0,1,0,0,1,1,1,0,2,2]
    print(s.profitableSchemes(test1, test2, test3, test4))