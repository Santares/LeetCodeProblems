from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        init = 1
        sums = 1
        for x in nums:
            sums += x
            if sums < 1:
                init += (1 - sums)
                sums = 1
        return init

    # online solution, faster
    def minStartValue2(self, nums: List[int]) -> int:
        minSum = nums[0]
        sums = nums[0]
        for i in range(1, len(nums)):
            sums += nums[i]
            if sums < minSum:
                minSum = sums
        return max(1 - minSum, 1)