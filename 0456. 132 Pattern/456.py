from typing import List


class Solution:
    # Online solution
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k = float('-inf')
        for x in nums[::-1]:
            if k != float('-inf') and x < k:
                return True
            while stack and stack[-1] < x:
                k = max(stack.pop(), k)
            stack.append(x)
        return False
