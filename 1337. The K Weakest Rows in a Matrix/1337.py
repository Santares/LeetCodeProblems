from heapq import heappush, heappop
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(len(mat)):
            x = sum(mat[i])
            heappush(heap, (x, i))

        res = []
        for i in range(k):
            x, index = heappop(heap)
            res.append(index)

        return res