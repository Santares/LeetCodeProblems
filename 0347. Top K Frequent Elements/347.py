from collections import defaultdict
from heapq import heappush, heappop
from typing import List
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for x in nums:
            freq[x] += 1

        # freq = collections.Counter(nums)

        heap = []
        for x in freq:
            heappush(heap, (-freq[x], x))

        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])

        return res
