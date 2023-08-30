from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        res = []
        record = [[[0, 0] for _ in range(n)] for _ in range(m)]

        queue1 = deque()  # pacific
        queue2 = deque()  # atlantic
        for i in range(m):
            queue1.append([i, 0])
            record[i][0][0] = 1
            queue2.append([i, n - 1])
            record[i][n - 1][1] = 1

        for j in range(n):
            queue1.append([0, j])
            record[0][j][0] = 1
            queue2.append([m - 1, j])
            record[m - 1][j][1] = 1

        while queue1:
            for _ in range(len(queue1)):
                x, y = queue1.pop()
                h = heights[x][y]
                for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        if heights[x + dx][y + dy] >= h and record[x + dx][y + dy][0] == 0:
                            record[x + dx][y + dy][0] = 1
                            queue1.append([x + dx, y + dy])

        while queue2:
            for _ in range(len(queue2)):
                x, y = queue2.pop()
                h = heights[x][y]
                for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        if heights[x + dx][y + dy] >= h and record[x + dx][y + dy][1] == 0:
                            record[x + dx][y + dy][1] = 1
                            queue2.append([x + dx, y + dy])

        for x in range(m):
            for y in range(n):
                if record[x][y][0] == 1 and record[x][y][1] == 1:
                    res.append([x, y])

        return res


if __name__ == '__main__':
    s = Solution()
    test = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    print(s.pacificAtlantic(test))
