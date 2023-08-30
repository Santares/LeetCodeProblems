from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]

        def dfs(x, y):
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                if 0 <= x + dx < m and 0 <= y + dy < n and visited[x + dx][y + dy] == 0:
                    visited[x + dx][y + dy] = 1
                    if grid[x + dx][y + dy] == '1':
                        dfs(x + dx, y + dy)

        res = 0
        for x in range(m):
            for y in range(n):
                if visited[x][y] == 1:
                    continue
                else:
                    if grid[x][y] == '1':
                        res += 1
                        visited[x][y] = 1
                        dfs(x, y)

        return res