from bisect import bisect_left
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        res = []
        for x in nums:
            if not res or res[-1] < x:
                res.append(x)
                if len(res) == 3:
                    return True
            else:
                index = bisect_left(res, x)
                res[index] = x

        return False

    # Based on online solution
    def increasingTriplet2(self, nums: List[int]) -> bool:
        first = nums[0]
        second = float('inf')
        for x in nums[1:]:
            if x > second:
                return True
            elif x > first:
                second = x
            else:
                first = x

        return False

    # Based on online solution
    def increasingTriplet3(self, nums: List[int]) -> bool:
        n = len(nums)
        leftMin = [0] * n
        rightMax = [0] * n

        for i, x in enumerate(nums):
            if i == 0:
                leftMin[i] = x
            else:
                leftMin[i] = min(leftMin[i - 1], x)

        for i in range(n - 1, -1, -1):
            x = nums[i]
            if i == n - 1:
                rightMax[i] = x
            else:
                rightMax[i] = max(rightMax[i + 1], x)

        for i in range(n):
            if nums[i] > leftMin[i] and nums[i] < rightMax[i]:
                return True

        return False
