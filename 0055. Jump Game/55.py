from typing import List


class Solution:
    # Online solution
    def canJump(self, nums: List[int]) -> bool:
        rightMost = 0
        for i in range(len(nums)):
            if i > rightMost:
                return False
            else:
                rightMost = max(rightMost, i + nums[i])
                if rightMost > len(nums) - 2:
                    return True

    # Online solution, DP
    def canJump2(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(len(nums)):
            if i > 0:
                dp[i] = max(dp[i - 1], i + nums[i])
            if dp[i] > len(nums) - 2:
                return True
            if dp[i] == i:
                return False
        return False
