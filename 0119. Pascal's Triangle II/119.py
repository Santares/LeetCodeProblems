from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = [1,1]
        for i in range(2,rowIndex+1):
            tmp = []
            for j in range(i-1):
                tmp.append(res[j] + res[j+1])
            res = [1] + tmp + [1]
        return res

