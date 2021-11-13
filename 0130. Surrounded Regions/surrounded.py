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


if __name__ == '__main__':
    solution = Solution()
    test = [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]]
    solution.solve(test)
    print(test)