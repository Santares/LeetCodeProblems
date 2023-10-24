from collections import defaultdict, deque
from typing import List


class Solution:
    # Too slow
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        nextCourses = defaultdict(list)
        dependCourses = defaultdict(int)
        for x, y in relations:
            nextCourses[x].append(y)
            dependCourses[y] += 1

        current = deque([])
        for i in range(1, n + 1):
            if dependCourses[i] == 0:
                current.append([i, time[i - 1]])

        t = 0
        while current:
            t += 1
            for _ in range(len(current)):
                course = current.popleft()
                course[1] -= 1
                if course[1] == 0:
                    for nxt in nextCourses[course[0]]:
                        dependCourses[nxt] -= 1
                        if dependCourses[nxt] == 0:
                            current.append([nxt, time[nxt - 1]])
                else:
                    current.append(course)

        return t

    # Improved version of solution 1, based on online solution
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        nextCourses = defaultdict(list)
        dependCourses = [0] * n
        finishTime = [0] * n
        for x, y in relations:
            nextCourses[x - 1].append(y - 1)
            dependCourses[y - 1] += 1

        current = deque()
        t = 0
        for i in range(n):
            if dependCourses[i] == 0:
                current.append(i)
                finishTime[i] = time[i]
                t = max(t, finishTime[i])

        while current:
            for _ in range(len(current)):
                course = current.popleft()
                for nxt in nextCourses[course]:
                    finishTime[nxt] = max(finishTime[nxt], finishTime[course] + time[nxt])
                    t = max(t, finishTime[nxt])
                    dependCourses[nxt] -= 1
                    if dependCourses[nxt] == 0:
                        current.append(nxt)

        return t


if __name__ == '__main__':
    s = Solution()
    n = 5
    test1 = [[1,5],[2,5],[3,5],[3,4],[4,5]]
    test2 = [1,2,3,4,5]
    print(s.minimumTime(n, test1, test2))