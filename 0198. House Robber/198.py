from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[i] = dp[i - 1]
            for j in range(i - 1):
                dp[i] = max(dp[i], dp[j] + nums[i - 1])

        return dp[-1]

    def rob2(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[-1]