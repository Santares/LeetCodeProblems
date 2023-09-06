from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        def helper(nums: List[int]) -> int:
            if len(nums) == 0:
                return 0
            dp = [0] * (len(nums) + 1)
            dp[0] = 0
            dp[1] = nums[0]
            for i in range(2, len(nums) + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

            return dp[-1]

        return max(helper(nums[:-1]), helper(nums[1:]))


if __name__ == '__main__':
    s = Solution()
    test = [1]
    print(s.rob(test))