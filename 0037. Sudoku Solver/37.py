from collections import defaultdict
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9

        rows = [defaultdict(bool) for _ in range(n)]
        cols = [defaultdict(bool) for _ in range(n)]
        subs = [defaultdict(bool) for _ in range(n)]

        def convert(i, j):
            return i // 3 * 3 + j // 3

        for i in range(n):
            for j in range(n):
                c = board[i][j]
                if c != '.':
                    rows[i][c] = True
                    cols[j][c] = True
                    subs[convert(i, j)][c] = True

        def isValid(i, j, c):
            return rows[i][c] == False and cols[j][c] == False and subs[convert(i, j)][c] == False

        def helper(index):
            if index >= n * n:
                return True

            i = index // n
            j = index % n

            if board[i][j] == '.':
                for x in range(1, 10):
                    c = str(x)
                    if isValid(i, j, c):
                        board[i][j] = c
                        rows[i][c] = True
                        cols[j][c] = True
                        subs[convert(i, j)][c] = True
                        if helper(index + 1):
                            return True
                        rows[i][c] = False
                        cols[j][c] = False
                        subs[convert(i, j)][c] = False
                        board[i][j] = '.'
                return False
            else:
                return helper(index + 1)

        helper(0)

        return
