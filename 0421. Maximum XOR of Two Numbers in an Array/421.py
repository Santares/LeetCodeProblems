from typing import List


class Solution:
    # Too slow
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                res = max(res, nums[i] ^ nums[j])

        return res