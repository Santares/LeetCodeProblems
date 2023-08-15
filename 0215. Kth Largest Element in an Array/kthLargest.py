import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[k * -1]

    # online solution
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

    # online solution
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    # Online solution
    def findKthLargest4(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
