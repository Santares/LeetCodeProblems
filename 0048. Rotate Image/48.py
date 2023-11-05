from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def helper(x, y, n):
            return [(y, n - x - 1), (n - x - 1, n - y - 1), (n - y - 1, x), (x, y)]

        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                index = helper(i, j, n)
                last = matrix[i][j]
                for x, y in index:
                    temp = matrix[x][y]
                    matrix[x][y] = last
                    last = temp
        return

    # Based on online solution
    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]

        for i in range(n // 2):
            matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]

        return


if __name__ == '__main__':
    s = Solution()
    test = [[5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]]
    print(s.rotate(test))
