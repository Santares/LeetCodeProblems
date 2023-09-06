from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        n = len(stones)

        dp = [[False] * (target+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        for i in range(n):
            for j in range(1, target+1):
                x = stones[i]
                if j >= x:
                    dp[i][j] = dp[i-1][j-x] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]


        for j in range(target, -1, -1):
            if dp[n-1][j]:
                return total - 2 * j

        return -1

    # reduce space
    def lastStoneWeightII2(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        n = len(stones)

        dp = [False] * (target + 1)
        dp[0] = True

        for x in stones:
            for j in range(target, 0, -1):
                if j >= x:
                    dp[j] = dp[j - x] or dp[j]

        for j in range(target, -1, -1):
            if dp[j]:
                return total - 2 * j

        return -1
