from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        right = 0
        res = 0
        currentRight = 0
        for i in range(len(nums) - 1):
            right = max(right, i + nums[i])

            if i == currentRight:
                res += 1
                currentRight = right

        return res

    # 2023/08/31
    def jump2(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(i):
            x = nums[i]
            s = 0
            rightMost = 0
            for j in range(x, 0, -1):
                if i + j >= n - 1:
                    return j
                else:
                    end = i + j + nums[i + j]
                    if end > rightMost:
                        rightMost = end
                        s = j
            return s

        i = 0
        res = 0
        while i < n - 1:
            s = helper(i)
            i += s
            res += 1

        return res
