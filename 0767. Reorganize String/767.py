from collections import Counter
from heapq import heappush, heappop


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = []
        for c in count:
            heappush(heap, [-count[c], c])

        res = ""
        last = heappop(heap)
        res += last[1]
        last[0] += 1
        while heap:
            cur = heappop(heap)
            res += cur[1]
            cur[0] += 1
            if last[0] < 0:
                heappush(heap, last)
            last = cur

        if last[0] == 0:
            return res
        else:
            return ""

    # Based on online solution
    def reorganizeString2(self, s: str) -> str:
        count = Counter(s)
        maxCount = count.most_common()[0][1]
        buckets = [""] * maxCount
        index = 0
        for c, cnt in count.most_common():
            for _ in range(cnt):
                buckets[index] += c
                index = (index + 1) % maxCount

        res = ""
        for i, bucket in enumerate(buckets):
            if len(bucket) == 1 and i < maxCount - 1:
                return ""
            else:
                res += bucket

        return res
