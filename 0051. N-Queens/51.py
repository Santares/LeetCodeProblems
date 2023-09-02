from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        used = [0] * n

        def isValid(x, y, exs):
            for i, j in exs:
                if i == x or y == j:
                    return False
                if abs(i - x) == abs(j - y):
                    return False

            return True

        def put(exs):
            grids = [['.'] * n for _ in range(n)]
            for x, y in exs:
                grids[x][y] = 'Q'
            grids = [''.join(row) for row in grids]
            res.append(grids)
            return

        def helper(i, cur):
            if i >= n:
                put(cur)
                return

            for j in range(n):
                if not used[j] and isValid(i, j, cur):
                    cur.append([i, j])
                    used[j] = True
                    helper(i + 1, cur)
                    cur.pop()
                    used[j] = False

        helper(0, [])

        return res

    [["5", "3", "1", "2", "7", "6", "4", "9", "8"],
     ["6", "2", "3", "1", "9", "5", "8", "4", "7"],
     ["1", "9", "8", "3", "4", "7", "5", "6", "2"],
     ["8", "1", "2", "7", "6", "4", "9", "5", "3"],
     ["4", "7", "9", "8", "5", "3", "6", "2", "1"],
     ["7", "4", "5", "9", "2", "8", "3", "1", "6"],
     ["9", "6", "7", "5", "3", "1", "2", "8", "4"],
     ["2", "8", "6", "4", "1", "9", "7", "3", "5"],
     ["3", "5", "4", "6", "8", "2", "1", "7", "9"]]

    [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
