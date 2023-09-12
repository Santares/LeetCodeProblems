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

    # Union find
    def numIslands(self, grid: List[List[str]]) -> int:
        parent = []
        roots = set()
        m = len(grid)
        n = len(grid[0])

        for x in range(m * n):
            parent.append(x)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                if x <= y:
                    parent[y] = x
                else:
                    parent[x] = y
            return

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        if 0 <= i + dx < m and 0 <= j + dy < n and grid[i + dx][j + dy] == '1':
                            union(i * n + j, (i + dx) * n + j + dy)

                    roots.add(parent[i * n + j])

        res = set([find(x) for x in roots])
        return len(res)


if __name__ == '__main__':
    s  = Solution()
    test = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    test = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    test = [["1"],["1"]]
    test = [["1","0","1","1","1"],
            ["1","0","1","0","1"],
            ["1","1","1","0","1"]]
    print(s.numIslands2(test))