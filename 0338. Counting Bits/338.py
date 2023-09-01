from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0, 1]

        if n <= 1:
            return res[:n + 1]

        flag = 4
        index = 0

        for i in range(2, n + 1):
            if i < flag:
                res.append(res[index] + 1)
                index += 1
            else:
                res.append(1)
                flag *= 2
                index = 1

        return res

    # Online solution
    def countBits2(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            res.append(res[i // 2] + i % 2)
        return res