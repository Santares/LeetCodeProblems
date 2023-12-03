from typing import List


class Solution:
    # Too slow
    def findDiagonalOrder0(self, nums: List[List[int]]) -> List[int]:
        res = []
        m = len(nums)
        n = max(len(row) for row in nums)

        for i in range(m):
            x = i
            y = 0
            while x >= 0:
                if y < len(nums[x]):
                    res.append(nums[x][y])
                x -= 1
                y += 1

        for i in range(1, n):
            x = m - 1
            y = i
            while x >= 0:
                if y < len(nums[x]):
                    res.append(nums[x][y])
                x -= 1
                y += 1

        return res

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        allNums = []
        for i, row in enumerate(nums):
            for j, x in enumerate(row):
                allNums.append((i, j, x))

        allNums.sort(key=lambda x: (x[0] + x[1], x[1], x[0]))

        return [x[2] for x in allNums]
