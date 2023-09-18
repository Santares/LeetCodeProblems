from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float("inf")
        for i in range(n - 2):
            j = i + 1
            k = n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    j += 1
                elif s == target:
                    return s
                else:
                    k -= 1
        return res


