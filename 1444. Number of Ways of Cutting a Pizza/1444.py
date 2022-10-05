from functools import lru_cache
from typing import List

class Solution:
    # slow
    def ways(self, pizza: List[str], k: int) -> int:
        n = len(pizza)
        m = len(pizza[0])

        count = [[-1] * n for _ in range(m)]

        queue = [(n - 1, m - 1)]
        while queue:
            temp = []
            for x, y in queue:
                left, right, inner = 0, 0, 0
                if x + 1 < n:
                    left = count[x + 1][y]
                if y + 1 < m:
                    right = count[x][y + 1]
                if x + 1 < n and y + 1 < m:
                    inner = count[x + 1][y + 1]

                if pizza[x][y] == 'A':
                    count[x][y] = 1 + left + right - inner
                else:
                    count[x][y] = left + right - inner

                for dx, dy in [(-1, 0), (0, -1), (0, 0)]:
                    if x + dx >= 0 and y + dy >= 0 and count[x + dx][y + dy] == -1:
                        temp.append((x + dx, y + dy))

            queue = list(temp)

        @lru_cache
        def helper(x, y, num):
            if num == 1:
                return 1

            res = 0

            for i in range(x + 1, n):
                if count[x][y] > count[i][y] and count[i][y] >= num - 1:
                    res += helper(i, y, num - 1)

            for j in range(y + 1, m):
                if count[x][y] > count[x][j] and count[x][j] >= num - 1:
                    res += helper(x, j, num - 1)

        return helper(0, 0, k)


if __name__ == '__main__':
    s = Solution()
    test1 = ["A..","AAA","..."]
    test2 = 3
    test1 = [".A","AA","A."]
    test2 = 3
    print(s.ways(test1, test2))
