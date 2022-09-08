from typing import List


class Solution:
    # slow
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] == target:
                return True
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1

        row = high

        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1

        return False

    # improved version based on online solution
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid = (left + right) // 2
            value = matrix[mid // m][mid % m]
            if value == target:
                return True
            elif target < value:
                right = mid - 1
            else:
                left = mid + 1

        return False


if __name__ == '__main__':
    s = Solution()
    test = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    test =[[1,3]]
    target = 3
    print(s.searchMatrix(test, target))
