from typing import List


class Solution:
    # slow
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0 or len(nums) < 2:
            return False

        target = total // 2

        dp = [[False] * (target + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True

        for i in range(len(nums)):
            for j in range(1, target + 1):
                if nums[i] == j:
                    dp[i][j] = True
                elif nums[i] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - nums[i]] or dp[i - 1][j]

        return dp[-1][-1]

    def canPartition2(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0 or len(nums) < 2:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for x in nums:
            for j in range(target, 0, -1):
                if j >= x:
                    dp[j] = dp[j - x] or dp[j]

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    test = [1,5,11,5]
    print(s.canPartition(test))