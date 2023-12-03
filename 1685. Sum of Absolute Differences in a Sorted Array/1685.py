from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        total = sum(nums)
        prefixSums = [0]
        for x in nums:
            prefixSums.append(x + prefixSums[-1])

        for i in range(n):
            x = nums[i] * i - prefixSums[i]
            x += prefixSums[n] - prefixSums[i + 1] - nums[i] * (n - i - 1)
            res.append(x)

        return res