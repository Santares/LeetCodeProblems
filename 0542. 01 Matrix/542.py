from collections import deque
from typing import List


class Solution:
    # dp
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        neg = m * n

        res = [[neg] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    if 0 <= i - 1 and res[i - 1][j] != neg:
                        res[i][j] = min(res[i][j], res[i - 1][j] + 1)
                    if 0 <= j - 1 and res[i][j - 1] != neg:
                        res[i][j] = min(res[i][j], res[i][j - 1] + 1)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i + 1 < m and res[i + 1][j] != neg:
                        res[i][j] = min(res[i][j], res[i + 1][j] + 1)
                    if j + 1 < n and res[i][j + 1] != neg:
                        res[i][j] = min(res[i][j], res[i][j + 1] + 1)

        return res

    # BFS
    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        queue = deque()

        neg = m * n
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        res = [[neg] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j))

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                if 0 <= x + dx < m and 0 <= y + dy < n and res[x + dx][y + dy] > 1 + res[x][y]:
                    res[x + dx][y + dy] = 1 + res[x][y]
                    queue.append((x + dx, y + dy))

        return res


if __name__ == '__main__':
    s = Solution()
    test = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    test = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
    print(s.updateMatrix(test))
