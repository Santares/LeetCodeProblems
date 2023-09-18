from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                m = (left + right) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    left = m + 1
                else:
                    right = m - 1
            return -1

        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1]:
                res = binarySearch(matrix[i], target)
                if res != -1:
                    return True
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        x = 0
        y = n - 1

        while x < m and y >= 0:
            num = matrix[x][y]
            if num == target:
                return True
            elif num < target:
                x += 1
            else:
                y -= 1

        return False
