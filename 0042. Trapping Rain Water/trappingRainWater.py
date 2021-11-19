from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        maxH = 0
        maxI = 0

        for i, x in enumerate(height):
            if x > maxH:
                maxH = x
                maxI = i

        res = 0
        bound = 0

        for i in range(maxI):
            h = height[i]
            if h < bound:
                res += bound - h
            else:
                bound = h

        bound = 0
        for j in range(len(height) - 1, maxI - 1, -1):
            h = height[j]
            if h < bound:
                res += bound - h
            else:
                bound = h

        return res

    # online solution, not faster
    def trap2(self, height: List[int]) -> int:
        N = len(height)
        if N < 3:
            return 0
        i, j = 0, N-1
        maxl, maxr = height[0], height[-1]
        res = 0
        while i < j:
            if height[i] < height[j]:
                if height[i] < maxl:
                    res += (maxl - height[i])
                else:
                    maxl = height[i]
                i += 1
            else:
                if height[j] < maxr:
                    res += (maxr - height[j])
                else:
                    maxr = height[j]
                j -= 1
        return res