from typing import List


class Solution:
    # Slow
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 1, 1
        res = [nums[0]]
        while right < len(nums):
            if nums[left] in res:
                if nums[right] in res:
                    right += 1
                else:
                    res.append(nums[right])
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right += 1
            else:
                res.append(nums[left])
                left += 1
                right += 1
        return left

    # Online solution
    def removeDuplicates2(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

    # My version of solution2
    def removeDuplicates3(self, nums: List[int]) -> int:
        left, right = 1, 1
        while right < len(nums):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left
