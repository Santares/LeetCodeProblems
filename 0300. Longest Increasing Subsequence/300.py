from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i, x in enumerate(nums):
            for j in range(i):
                if x > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    # Based on online solution, much faster
    def lengthOfLIS2(self, nums: List[int]) -> int:
        res = [nums[0]]
        rLen = 1

        def helper(l, r, k, nums):
            res = r
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= k:
                    res = m
                    r = m - 1
                else:
                    l = m + 1
            return res

        for i in range(1, len(nums)):
            x = nums[i]
            if x > res[-1]:
                res.append(x)
                rLen += 1
            elif x == res[-1]:
                continue
            else:
                index = helper(0, rLen-1, x, res)
                res[index] = x

        return rLen


if __name__ == '__main__':
    s = Solution()
    test = [1,7,8,2,3,4]
    print(s.lengthOfLIS2(test))
