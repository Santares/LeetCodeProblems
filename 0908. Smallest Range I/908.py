from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        snums = sorted(nums)
        if snums[-1] - snums[0] <= 2 * k:
            return 0

        return snums[-1] - 2 * k - snums[0]

    # online solution
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)