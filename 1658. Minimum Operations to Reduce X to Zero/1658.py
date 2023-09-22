from typing import List


class Solution:
    # Hash table + prefix sum
    def minOperations(self, nums: List[int], x: int) -> int:
        dic = {0: 0}
        total = 0
        n = len(nums)
        for i in range(1, n + 1):
            total += nums[n - i]
            dic[total] = i

        total = 0
        nums = [0] + nums
        res = float('inf')
        for i in range(n + 1):
            total += nums[i]
            if x - total in dic and i + dic[x - total] <= n:
                res = min(res, i + dic[x - total])

        return -1 if res == float('inf') else res

    # Two pointers / sliding window. Reverse approach
    def minOperations2(self, nums: List[int], x: int) -> int:
        def helper(nums, target):
            left = 0
            res = 0
            total = 0
            for right in range(len(nums)):
                total += nums[right]
                while total > target:
                    total -= nums[left]
                    left += 1

                if target == total:
                    res = max(res, right - left + 1)

            return res

        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        n = helper(nums, target)
        if n == 0:
            return -1

        return len(nums) - n

    # Based on online solution. Sliding window, O(N)
    def minOperations3(self, nums: List[int], x: int) -> int:
        leftSums = [0]
        rightSums = [0]
        n = len(nums)
        for i in range(n):
            leftSums.append(leftSums[-1] + nums[i])
            rightSums.append(rightSums[-1] + nums[n - 1 - i])

        rightSums = rightSums[::-1]

        res = float('inf')
        left = 0
        right = 0
        while right < n + 1 and left <= right:
            total = leftSums[left] + rightSums[right]
            if total == x:
                res = min(res, (left + (n - right)))
                right += 1
                left += 1
            elif total > x:
                right += 1
            else:
                left += 1

        return res if res != float('inf') else -1



