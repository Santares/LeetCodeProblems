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


if __name__ == '__main__':
    s = Solution()
    nums = [2,3,1,2,4,3]
    target = 7
    print(s.minSubArrayLen(target, nums))
