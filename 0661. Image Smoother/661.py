from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        sums = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sums[i][j] = img[i - 1][j - 1] + sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1]

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                a = max(i - 1, 0)
                b = min(i + 1, m - 1)
                c = max(j - 1, 0)
                d = min(j + 1, n - 1)
                count = (b - a + 1) * (d - c + 1)
                total = sums[b + 1][d + 1] - sums[b + 1][c] - sums[a][d + 1] + sums[a][c]
                res[i][j] = total // count

        return res

if __name__ == '__main__':
    s = Solution()
    test1 = [[1,1,1],[1,0,1],[1,1,1]]
    print(s.imageSmoother(test1))
