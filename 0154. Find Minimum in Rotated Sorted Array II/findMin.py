from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

    def findMin2(self, nums: List[int]) -> int:
        last = nums[0]
        for x in nums:
            if x < last:
                return x
            else:
                last = x
        return nums[0]
