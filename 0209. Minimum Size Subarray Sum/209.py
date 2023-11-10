from bisect import bisect_left
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        last = 0
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]
            while left < len(nums):
                if sum - nums[left] >= target:
                    sum -= nums[left]
                    left += 1
                else:
                    break

            if sum >= target:
                length = right - left + 1
                if last == 0 or (last != 0 and length < last):
                    last = length
        return last

    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        left = 0
        res = float('inf')
        total = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1

        return res if res != float('inf') else 0

    # binary search, O(nlogn)
    def minSubArrayLen3(self, target: int, nums: List[int]) -> int:
        sums = nums.copy()
        for i in range(1, len(nums)):
            sums[i] += sums[i - 1]
        sums = [0] + sums

        def binarySearch(nums, left, right, target):
            res = -1
            while left <= right:
                m = (left + right) // 2
                if sums[m] <= target:
                    res = m
                    left = m + 1
                else:
                    right = m - 1
            return res

        res = float('inf')
        newTarget = sum(nums) - target

        nums.append(0)
        for j in range(len(nums) - 1, 0, -1):
            newTarget -= nums[j]
            index = binarySearch(sums, 0, j - 1, newTarget)
            if index != -1:
                res = min(res, j - index)

        return res if res != float('inf') else 0

    # 20231106 binary search
    def minSubArrayLen4(self, target: int, nums: List[int]) -> int:
        sums = [0]
        for x in nums:
            sums.append(sums[-1] + x)

        if target > sums[-1]:
            return 0

        res = float('inf')
        for i in range(len(sums) - 1):
            index = bisect_left(sums, target + sums[i])
            if index < len(sums):
                res = min(res, index - i)
        return res

    # sliding window (two pointers)
    def minSubArrayLen5(self, target: int, nums: List[int]) -> int:
        if target > sum(nums):
            return 0
        left = 0
        n = len(nums)
        cur = 0
        res = n + 1
        for right in range(n):
            cur += nums[right]
            while cur >= target:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1

        return res


if __name__ == '__main__':
    s = Solution()
    nums = [2,3,1,2,4,3]
    target = 7
    # nums = [1,2,3,4,5]
    # target = 11
    print(s.minSubArrayLen3(target, nums))
