from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        if rows == 0:
            return

        cols = len(board[0])
        queue = []

        for j in range(cols):
            if board[0][j] == 'O':
                queue.append([0, j])
            if board[rows - 1][j] == 'O':
                queue.append([rows - 1, j])
        for i in range(1, rows - 1):
            if board[i][0] == 'O':
                queue.append([i, 0])
            if board[i][cols - 1] == 'O':
                queue.append([i, cols - 1])

        while queue:
            pos = queue.pop(0)

            x = pos[0]
            y = pos[1]
            board[x][y] = 'R'

            if x - 1 >= 0:
                if board[x - 1][y] == 'O':
                    queue.append([x - 1, y])
            if x + 1 < rows:
                if board[x + 1][y] == 'O':
                    queue.append([x + 1, y])
            if y - 1 >= 0:
                if board[x][y - 1] == 'O':
                    queue.append([x, y - 1])
            if y + 1 < cols:
                if board[x][y + 1] == 'O':
                    queue.append([x, y + 1])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "R":
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    # Union find
    def solve2(self, board: List[List[str]]) -> None:
        def find(x):
            while root[x] != x:
                x = root[x]
            return x

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                if x < y:
                    root[y] = x
                else:
                    root[x] = y

        m = len(board)
        n = len(board[0])
        root = {x: x for x in range(m * n)}
        root[-1] = -1

        dummy = -1

        for i in range(m):
            if board[i][0] == 'O':
                union(dummy, i * n)
            if board[i][n - 1] == 'O':
                union(dummy, i * n + n - 1)

        for j in range(n):
            if board[0][j] == 'O':
                union(dummy, j)
            if board[m - 1][j] == 'O':
                union(dummy, (m - 1) * n + j)

        for x in range(m):
            for y in range(n):
                if board[x][y] == 'O':
                    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        if 0 <= x + dx < m and 0 <= y + dy < n and board[x + dx][y + dy] == 'O':
                            union(x * n + y, (x + dx) * n + y + dy)

        for i in range(m):
            for j in range(n):
                if find(i * n + j) != -1:
                    board[i][j] = 'X'


if __name__ == '__main__':
    solution = Solution()
    test = [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]]
    test = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
    solution.solve2(test)
    print(test)