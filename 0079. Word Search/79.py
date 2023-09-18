from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(word)
        m = len(board)
        n = len(board[0])

        def search(x, y, index):
            if index == l:
                return True
            res = False
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= x + dx < m and 0 <= y + dy < n and not visited[x + dx][y + dy]:
                    if board[x + dx][y + dy] == word[index]:
                        visited[x + dx][y + dy] = True
                        res = search(x + dx, y + dy, index + 1)
                        if res:
                            break
                        visited[x + dx][y + dy] = False
            return res

        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if search(i, j, 1):
                        return True
                    visited[i][j] = False

        return False
