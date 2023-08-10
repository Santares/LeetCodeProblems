from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        leftLimit = 0
        rightLimit = len(matrix[0]) - 1
        topLimit = 1
        bottomLimit = len(matrix) - 1
        # 0: right, 1: down, 2: left, 3: up
        direction = 0

        i = 0
        j = 0
        while True:
            res.append(matrix[i][j])
            if direction == 0:
                if j >= rightLimit:
                    i += 1
                    if i > bottomLimit:
                        break
                    direction = 1
                    rightLimit -= 1
                else:
                    j += 1
            elif direction == 1:
                if i >= bottomLimit:
                    j -= 1
                    if j < leftLimit:
                        break
                    direction = 2
                    bottomLimit -= 1
                else:
                    i += 1
            elif direction == 2:
                if j <= leftLimit:
                    i -= 1
                    if i < topLimit:
                        break
                    direction = 3
                    leftLimit += 1
                else:
                    j -= 1
            else:
                if i <= topLimit:
                    j += 1
                    if j > rightLimit:
                        break
                    direction = 0
                    topLimit += 1
                else:
                    i -= 1

        return res

    # Online solution
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            # 削头（第一层）
            res += matrix.pop(0)
            # 将剩下的逆时针转九十度，等待下次被削
            # zip(*matrix) equals transpose the matrix
            matrix = list(zip(*matrix))[::-1]
        return res



if __name__ == '__main__':
    s = Solution()
    test = [[1,2,3],[4,5,6],[7,8,9]]
    test = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(s.spiralOrder(test))