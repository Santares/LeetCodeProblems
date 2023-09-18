from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            m = (left + right) // 2

            # Find min, compare m and m - 1
            if m > 0 and nums[m - 1] > nums[m]:
                return nums[m]

            # Find min, compare m and right
            elif nums[m] < nums[right]:
                right = m - 1
            else:
                left = m + 1

        # Doesn't matter
        return nums[left - 1]

    def findMin2(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            m = (left + right) // 2

            # Find max, compare m and m + 1
            if nums[m + 1] < nums[m]:
                return nums[m + 1]

            # Find max, compare m and left
            elif nums[m] < nums[left]:
                right = m - 1

            else:
                left = m + 1

        # Doesn't matter
        return nums[left]

    # Online solution
    def findMin3(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left < right:
            m = (left + right) // 2

            if nums[m] > nums[right]:  # 中值 > 右值，最小值在右半边，收缩左边界
                left = m + 1  # 因为中值 > 右值，中值肯定不是最小值，左边界可以跨过mid
            elif nums[m] < nums[right]:  # 明确中值 < 右值，最小值在左半边，收缩右边界
                right = m

        return nums[left]

