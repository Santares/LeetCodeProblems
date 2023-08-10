from typing import List


class Solution:
    # Not wrong
    def search(self, nums: List[int], target: int) -> bool:
        def helper(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return False

        nums.sort()

        return helper(nums, target)

    # Based on problem 33 solution4
    def search2(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            # Left is sorted
            elif nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Not sure
            elif nums[left] == nums[mid]:
                left += 1
            # Right is sorted
            else:
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False