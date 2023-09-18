from typing import List


class Solution:
    # Based on online solution2
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]
        left = 1
        right = len(nums) - 2

        while left <= right:
            m = (left + right) // 2
            if nums[m - 1] < nums[m] and nums[m] > nums[m + 1]:
                return m - 1
            elif nums[m] < nums[m + 1]:
                left = m + 1
            else:
                right = m - 1

        return False