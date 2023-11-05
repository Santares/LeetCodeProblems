from typing import List


class Solution:
    # Based on online solution
    def maxProduct(self, nums: List[int]) -> int:
        maxs = nums.copy()
        mins = nums.copy()
        for i in range(1, len(nums)):
            maxs[i] = max(maxs[i-1] * nums[i], mins[i-1] * nums[i], nums[i])
            mins[i] = min(maxs[i-1] * nums[i], mins[i-1] * nums[i], nums[i])

        return max(maxs)

    # Save space
    def maxProduct2(self, nums: List[int]) -> int:
        lastMax = nums[0]
        lastMin = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            newMax = max(lastMax * nums[i], lastMin * nums[i], nums[i])
            newMin = min(lastMax * nums[i], lastMin * nums[i], nums[i])
            lastMax = newMax
            lastMin = newMin
            res = max(res, newMax)

        return res