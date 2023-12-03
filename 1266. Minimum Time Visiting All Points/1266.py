import random
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def distance(A, B):
            x1, y1 = A[0], A[1]
            x2, y2 = B[0], B[1]
            return max(abs(x1 - x2), abs(y1 - y2))

        res = 0
        last = points[0]
        for cur in points[1:]:
            res += distance(last, cur)
            last = cur

        return res


def distance(A, B):
    x1, y1 = A[0], A[1]
    x2, y2 = B[0], B[1]
    return max(abs(x1 - x2), abs(y1 - y2))


def distance2(A, B):
    x1, y1 = A[0], A[1]
    x2, y2 = B[0], B[1]
    return min(
        abs(x1 - x2) + abs(y1 - (x1 - x2) - y2),
        abs(y1 - y2) + abs(x1 - (y1 - y2) - x2)
    )

def distance3(A, B):
    x1, y1 = A[0], A[1]
    x2, y2 = B[0], B[1]

    res = 0
    a = (y1-x1) - (y2-x2)
    res += abs(a)
    res += min(abs(x1-x2), abs(y1-y2))
    return res


if __name__ == '__main__':
    # while True:
    #     A = [random.randint(-10, 10), random.randint(-10, 10)]
    #     B = [random.randint(-10, 10), random.randint(-10, 10)]
    #     if distance(A, B) != distance2(A,B):
    #         print(A)
    #         print(B)
    #         break
    A = [-5, 9]
    B = [2, 7]
    print(distance(A, B))
    print(distance2(A, B))
    print(distance3(A,B))
