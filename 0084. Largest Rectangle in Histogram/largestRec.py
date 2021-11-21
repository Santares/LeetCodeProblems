from typing import List


class Solution:
    # too slow
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)

        res = 0

        for i in range(l):
            h = heights[i]
            temp = 1
            for j in range(i - 1, -1, -1):
                if heights[j] >= h:
                    temp += 1
                else:
                    break
            for j in range(i + 1, l):
                if heights[j] >= h:
                    temp += 1
                else:
                    break

            res = max(res, temp * h)

        return res

    # acceptable, slow
    def largestRectangleArea2(self, heights: List[int]) -> int:
        queue = [[heights[0], 1]]
        res = 0

        for x in heights[1:]:
            count = 0
            for j in range(len(queue) - 1, -1, -1):
                if x > queue[j][0]:
                    queue[j][1] += 1
                else:
                    res = max(res, queue[j][1] * queue[j][0])
                    count = queue[j][1]
                    queue.pop()
            queue.append([x, count + 1])

        while queue:
            h, c = queue.pop()
            res = max(res, h * c)

        return res

    # online solution, faster
    def largestRectangleArea3(self, heights: List[int]) -> int:
        l = len(heights)
        res = 0
        leftBound = [-1] * l
        rightBound = [l] * l

        for i in range(1, l):
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                j = leftBound[j]
            leftBound[i] = j

        for i in range(l - 2, -1, -1):
            j = i + 1
            while j < l and heights[j] >= heights[i]:
                j = rightBound[j]
            rightBound[i] = j

        for i in range(l):
            res = max(res, heights[i] * (rightBound[i] - leftBound[i] - 1))

        return res

    # online solution
    def largestRectangleArea4(self, heights: List[int]) -> int:
        # heights.append(0) # important
        queue = [-1, 0]
        res = 0
        l = len(heights)

        for i in range(1, l):
            while True:
                j = queue[-1]
                if queue[-1] >= 0 and heights[i] <= heights[j]:
                # if heights[i] <= heights[j]: # this will make this solution much faster
                    queue.pop()
                    res = max(res,  heights[j] * (i - queue[-1] - 1))
                else:
                    break
            queue.append(i)

        return res

    # online solution, much faster
    def largestRectangleArea5(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans


if __name__ == '__main__':
    solution = Solution()
    test = [2,1,5,6,2,3]
    test = [2,4]

    print(solution.largestRectangleArea4(test))





