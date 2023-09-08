from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for row in range(1, numRows + 1):
            cur = []
            for i in range(row):
                if i == 0 or i == row - 1:
                    cur.append(1)
                else:
                    cur.append(res[-1][i - 1] + res[-1][i])

            res.append(cur)

        return res
