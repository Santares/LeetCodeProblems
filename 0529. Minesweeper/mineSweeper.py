from typing import List

class Solution:
    # too slow
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])

        def adjacentMine(x, y, visited):
            count = 0
            adjacent = []
            for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    if board[x + dx][y + dy] == 'M':
                        count += 1
                    if visited[x + dx][y + dy] == 0:
                        adjacent.append([x + dx, y + dy])
            return count, adjacent

        row = click[0]
        col = click[1]
        if board[row][col] == 'M':
            board[row][col] = 'X'
        elif board[row][col] == 'E':
            visited = [[0] * n for _ in range(m)]
            queue = [[row, col]]
            while queue:
                temp = []
                for x, y in queue:
                    visited[x][y] = 1
                    mineCount, newAdjacent = adjacentMine(x, y, visited)
                    if mineCount != 0:
                        board[x][y] = str(mineCount)
                        continue
                    else:
                        board[x][y] = 'B'
                        temp += newAdjacent

                queue = list(temp)
                temp.clear()

        return board

    # very fast
    def updateBoard2(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])

        row = click[0]
        col = click[1]
        if board[row][col] == 'M':
            board[row][col] = 'X'
        elif board[row][col] == 'E':
            visited = [[0] * n for _ in range(m)]
            queue = [[row, col]]
            while queue:
                temp = []
                for x, y in queue:
                    if visited[x][y] == 1:  # crucial!!
                        continue
                    visited[x][y] = 1
                    mineCount = 0
                    adjacent = []
                    for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                        if 0 <= x + dx < m and 0 <= y + dy < n:
                            if board[x + dx][y + dy] == 'M':
                                mineCount += 1
                            if visited[x + dx][y + dy] == 0:
                                adjacent.append([x + dx, y + dy])
                    if mineCount != 0:
                        board[x][y] = str(mineCount)
                        continue
                    else:
                        board[x][y] = 'B'
                        temp += adjacent

                queue = list(temp)
                temp.clear()

        return board

    # online solution
    def updateBoard3(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        m, n = len(board), len(board[0])

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return

            # count neighbor mines
            mineCnt = 0
            for i, j in directions:
                r, c = row + i, col + j
                if 0 <= r < m and 0 <= c < n and board[r][c] == 'M':
                    mineCnt += 1

            if mineCnt == 0:
                board[row][col] = 'B'
                # dfs neighbor cells
                for i, j in directions:
                    r, c = row + i, col + j
                    # only dfs for unvisited cells
                    if 0 <= r < m and 0 <= c < n and board[r][c] == 'E':
                        dfs(r, c)
            else:
                board[row][col] = str(mineCnt)

        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            dfs(r, c)
        return board