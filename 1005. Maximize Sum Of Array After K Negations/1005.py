from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -1 * nums[i]
                k -= 1

        res = sum(nums)
        if k > 0 and k % 2 == 1:
            res -= 2 * min(nums)

        return res