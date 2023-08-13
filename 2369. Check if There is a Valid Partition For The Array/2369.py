from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [0] * (len(nums) - 1)
        dp.append(-1)
        dp.append(1)
        length = len(nums)

        def helper(index):
            if dp[index] != 0:
                return False if dp[index] == -1 else True

            res = False

            if nums[index] == nums[index + 1]:
                res = res or helper(index + 2)

            if index + 2 < length:
                if (nums[index] == nums[index + 1] == nums[index + 2]) or (
                        nums[index] == nums[index + 1] - 1 == nums[index + 2] - 2):
                    res = res or helper(index + 3)

            dp[index] = 1 if res else -1

            return res

        return helper(0)

    # Online solution
    def validPartition2(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n + 1)]  # dp[i+1]表示[0,i]是否可以被成功划分
        dp[0] = True
        for i in range(1, n):
            if nums[i] == nums[i - 1] and dp[i - 1]:
                dp[i + 1] = True
            if i > 1:
                if nums[i] == nums[i - 1] == nums[i - 2] and dp[i - 2]:
                    dp[i + 1] = True
                if nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2 and dp[i - 2]:
                    dp[i + 1] = True
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    test = [865579,865579,893593]
    print(s.validPartition(test))