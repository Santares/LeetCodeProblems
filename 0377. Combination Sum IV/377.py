from functools import cache
from typing import List


class Solution:
    # Backtrace, slow
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.res = 0

        def helper(cur):
            if cur > target:
                return
            if cur == target:
                self.res += 1
                return

            for x in nums:
                helper(cur + x)

        helper(0)

        return self.res

    # Improved version of solution 1
    def combinationSum42(self, nums: List[int], target: int) -> int:
        @cache
        def helper(cur):
            if cur > target:
                return 0
            if cur == target:
                return 1

            res = 0
            for x in nums:
                res += helper(cur + x)
            return res

        return helper(0)

    # DP
    def combinationSum43(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for x in nums:
                if x <= i:
                    dp[i] += dp[i - x]

        return dp[-1]

    # Based on online solution
    def combinationSum44(self, nums: List[int], target: int) -> int:
        @cache
        def helper(target):
            if target == 0:
                return 1
            res = 0
            for x in nums:
                if x <= target:
                    res += helper(target - x)
            return res

        return helper(target)
