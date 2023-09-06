from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] += dp[i - 1]

        return max(dp)

    def findLengthOfLCIS2(self, nums: List[int]) -> int:
        res = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1

        return res
