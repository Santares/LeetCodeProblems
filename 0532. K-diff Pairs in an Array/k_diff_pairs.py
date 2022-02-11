from collections import Counter
from typing import List


class Solution:

    # slow
    def findPairs(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0

        left = 0
        right = 1
        res = 0

        nums.sort()
        used = []

        while right < len(nums):
            if left == right:
                right += 1
                continue

            diff = nums[right] - nums[left]
            if diff == k:
                if nums[right] in used:
                    right += 1
                else:
                    res += 1
                    used.append(nums[right])
                    right += 1
            elif diff < k:
                right += 1
            else:
                left += 1

        return res

    # online
    def findPairs2(self, nums: List[int], k: int) -> int:
        # if len(nums) < 2:
        #     return 0

        res = 0

        num_set = Counter(nums)
        if k == 0:
            for x in num_set:
                if num_set[x] > 1:
                    res += 1
        else:
            for x in num_set:
                if x + k in num_set:
                    res += 1

        return res

    # online solution, much faster
    def findPairs3(self, nums, k):
        res = 0
        if k == 0:
            cnt = Counter(nums)
            for x in cnt:
                if cnt[x] > 1: res += 1
        else:
            ms = set(nums)
            for x in ms:
                if x + k in ms: res+=1
        return res

    # improved of 1, much faster
    def findPairs4(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0

        left = 0
        right = 1
        res = 0

        nums.sort()

        while right < len(nums):
            if left == right:
                right += 1
                continue

            diff = nums[right] - nums[left]
            if diff == k:
                res += 1
                right += 1
                while right < len(nums):
                    if nums[right - 1] == nums[right]:
                        right += 1
                    else:
                        break
            elif diff < k:
                right += 1
            else:
                left += 1

        return res