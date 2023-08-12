from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        dp = [[-1] * columns for _ in range(rows)]
        dp[-1][-1] = 1

        def helper(x, y):
            if not (0 <= x < rows and 0 <= y < columns):
                return 0

            if dp[x][y] != -1:
                return dp[x][y]

            res = 0
            if obstacleGrid[x][y] != 1:
                res = helper(x + 1, y) + helper(x, y + 1)

            dp[x][y] = res
            return res

        return helper(0, 0)

    # Online solution
    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]

        return dp[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    test = [[0,0,0],[0,1,0],[0,0,0]]
    print(s.uniquePathsWithObstacles((test)))