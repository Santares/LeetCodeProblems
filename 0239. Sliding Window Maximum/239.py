from collections import deque
from typing import List


class Solution:
    # monotonic queue
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        for i in range(len(nums)):

            while queue and queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if i >= k - 1:
                res.append(nums[queue[0]])

        return res

    # Max Heap
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i in range(k):
            heappush(heap, (-1 * nums[i], i))

        res.append(heap[0][0])
        for i in range(k, len(nums)):
            heappush(heap, (-1 * nums[i], i))
            while heap[0][1] <= i - k:
                heappop(heap)

            res.append(heap[0][0])

        return [-1 * x for x in res]

