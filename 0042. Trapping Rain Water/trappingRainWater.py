from collections import deque
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
        i, j = 0, N - 1
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

    # 2023/08/23
    def trap3(self, height: List[int]) -> int:
        def helper(height):
            record = [-1] * len(height)

            queue = deque()
            for i, x in enumerate(height):
                while queue and height[queue[-1]] <= x:
                    record[queue.pop()] = i
                queue.append(i)

            res = 0
            i = 0
            while i < len(height):
                if record[i] != -1:
                    h = min(height[i], height[record[i]])
                    for j in range(i + 1, record[i]):
                        res += h - height[j]

                    i = record[i]
                else:
                    i += 1

            return res

        highest = 0
        for i, x in enumerate(height):
            if x > height[highest]:
                highest = i

        return helper(height[:highest + 1]) + helper(height[highest:][::-1])

    # Improved version of solution3, monotonic stack, based on online solution
    def trap4(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, x in enumerate(height):
            while stack and height[stack[-1]] < x:
                mid = stack.pop()
                if stack:
                    h = min(height[stack[-1]], x) - height[mid]
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)

        return res

    # Based on online solution, dp
    def trap5(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        leftMax[0] = height[0]
        rightMax[-1] = height[-1]

        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i - 1], height[i])

        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        res = 0
        for i, x in enumerate(height):
            res += min(leftMax[i], rightMax[i]) - x

        return res

    # Another version of solution2, two pointers
    def trap6(self, height: List[int]) -> int:
        left = 1
        right = len(height) - 2
        leftMax = height[0]
        rightMax = height[-1]

        res = 0

        while left <= right:
            if leftMax < rightMax:
                res += max(0, leftMax - height[left])
                leftMax = max(leftMax, height[left])
                left += 1
            else:
                res += max(0, rightMax - height[right])
                rightMax = max(rightMax, height[right])
                right -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    test = [4, 2, 3]
    print(s.trap5(test))
