from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memory = [defaultdict(int) for _ in range(len(nums))]
        memory[0][nums[0]] += 1
        memory[0][-nums[0]] += 1

        for i in range(1, len(nums)):
            x = nums[i]
            for item in memory[i - 1].items():
                memory[i][item[0] + x] += item[1]
                memory[i][item[0] - x] += item[1]

        return memory[-1][target]

    # Backtrace, too slow
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        self.res = 0
        n = len(nums)

        def helper(i, cur):
            if i >= n:
                if cur == target:
                    self.res += 1
                return

            x = nums[i]
            helper(i + 1, cur + x)
            helper(i + 1, cur - x)

        helper(0, 0)

        return self.res

    # DP
    def findTargetSumWays3(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < target or (total - target) % 2 != 0:
            return 0

        target = (total - target) // 2

        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(target + 1):
                x = nums[i - 1]
                if x <= j:
                    dp[i][j] = dp[i - 1][j - x] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    test1 = [1,1,1,1,1,]
    test2 = 3
    print(s.findTargetSumWays(test1, test2))