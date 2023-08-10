from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        directionIndex = 0
        x, y = 0, 0

        for i in range(n * n):
            res[x][y] = i+1
            dx, dy = directions[directionIndex]
            if 0 <= x + dx < n and 0 <= y + dy < n and res[x + dx][y + dy] == 0:
                x += dx
                y += dy
            else:
                directionIndex = (directionIndex + 1) % 4
                dx, dy = directions[directionIndex]
                x += dx
                y += dy

        return res


if __name__ == '__main__':
    s = Solution()
    test = 3
    print(s.generateMatrix(test))