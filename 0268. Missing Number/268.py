from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        base = nums[0]

        if nums[0] != 0:
            return 0
        if nums[-1] != base + len(nums):
            return base + len(nums)

        while left < right:
            mid = right + (left - right) // 2
            if nums[mid] == base + mid:
                left = mid + 1
            elif nums[mid] > base + mid:
                right = mid

        return left


    # online solution
    def missingNumber2(self, nums):
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)