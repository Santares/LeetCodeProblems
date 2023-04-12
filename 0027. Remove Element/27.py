from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                if nums[right] != val:
                    nums[left] = nums[right]
                    left += 1
                right -= 1
            else:
                left += 1
        return left

    # online solution. Fast & slow pointers
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left

