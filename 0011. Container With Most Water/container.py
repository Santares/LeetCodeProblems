from typing import List


class Solution:
    # slow
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height)

        return max((len(height) - 1) * min(height[0], height[-1]),
                   self.maxArea(height[:-1]),
                   self.maxArea(height[1:]))

    # slow
    def maxArea2(self, height: List[int]) -> int:
        self.record = [[0] * len(height) for _ in range(len(height))]

        def helper(i, j):
            if self.record[i][j] != 0:
                return self.record[i][j]

            if i + 1 == j:
                self.record[i][j] = min(height[i], height[j])
            else:
                self.record[i][j] = max((j - i) * min(height[i], height[j]),
                                        helper(i + 1, j), helper(i, j - 1))
            return self.record[i][j]

        helper(0, len(height) - 1)

        return self.record[0][len(height) - 1]

    # wrong
    def maxArea3(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        # res = (right - left) * min(height[left], height[right])
        n = len(height)
        sortedHeight = sorted(height)
        largest = sortedHeight[-1]
        second = sortedHeight[-2]
        left = -1
        right = -1
        for i in range(n):
            x = height[i]
            if x == largest:
                left = i
            if x == second:
                if second == right and left == i:
                    continue
                else:
                    right = i
            if right >= 0 and left >= 0:
                break

        if left > right:
            left, right = right, left

        res = (right - left) * min(height[left], height[right])

        if height[left] < height [right]:
            i = left
            while i >= 0:
                area = max(res, (right - i) * min(height[right], height[i]))
                if area > res:
                    res = area
                    left = i
                i -= 1
        else:
            j = right
            while j < n:
                area = max(res, (j - left) * min(height[j], height[left]))
                if area > res:
                    res = area
                    right = j
                j += 1


        j = right
        while j < n:
            area = max(res, (j-left) * min(height[j], height[left]))
            if area > res:
                res = area
                right = j
            j += 1
        i = left
        while i >= 0:
            res = max(res, (right - i) * min(height[right], height[i]))
            i -= 1

        return res

    # slow
    def maxArea4(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] <= height[right]:
                left += 1
                res = max(res, (right - left) * min(height[left], height[right]))
            else:
                right -= 1
                res = max(res, (right - left) * min(height[left], height[right]))
        return res

if __name__ == '__main__':
    solution = Solution()
    test = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    test = [1,1]
    test = [2,3,4,5,18,17,6]
    test = [4,4,2,11,0,11,5,11,13,8]
    print(solution.maxArea3(test))
