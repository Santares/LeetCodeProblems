from typing import List


class Solution:
    # too slow
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [0]
        for x in nums:
            sums.append(sums[-1] + x)

        res = -10000
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                temp = sums[j] - sums[i]
                res = max(res, temp)

        return res

    # not bad
    def maxSubArray2(self, nums: List[int]) -> int:
        res = [nums[0]]
        sums = nums[0]
        maxSum = sums
        for x in nums[1:]:
            if sums + x <= x:
                res = [x]
                sums = x
            elif x > res[0] and res[0] <= 0:
                res.append(x)
                sums -= res.pop(0)
                sums += x
            else:
                res.append(x)
                sums += x
            maxSum = max(sums, maxSum)

        return maxSum

    # "DP", not faster
    def maxSubArray2(self, nums: List[int]) -> int:
        last = nums[0]
        res = last

        for x in nums[1:]:
            last = max(last + x, x)
            res = max(last, res)

        return res

    # improved #1
    def maxSubArray3(self, nums: List[int]) -> int:
        sums = nums[0]
        maxSum = sums
        for x in nums[1:]:
            if sums + x <= x:
                sums = x
            else:
                sums += x
            maxSum = max(sums, maxSum)

        return maxSum