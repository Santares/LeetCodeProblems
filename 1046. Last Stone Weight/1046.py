from heapq import heappush, heappop
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for x in stones:
            heappush(heap, -x)

        while heap:
            if len(heap) >= 2:
                a = heappop(heap) * -1
                b = heappop(heap) * -1
                if a != b:
                    heappush(heap, (-1 * (a - b)))
            else:
                return -1 * heap[0]

        return 0


