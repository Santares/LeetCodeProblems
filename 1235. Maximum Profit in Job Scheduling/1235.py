from bisect import bisect, bisect_left
from collections import defaultdict
from typing import List


class Solution:
    # Memory limit exceeded
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = defaultdict(list)
        for i in range(n):
            jobs[startTime[i]].append([endTime[i], profit[i]])

        m = max(endTime)
        dp = [0] * (m + 1)
        for i in range(1, m+1):
            if i > 0:
                dp[i] = max(dp[i], dp[i - 1])
            for job in jobs[i]:
                end = job[0]
                pro = job[1]
                dp[end] = max(dp[end], dp[i] + pro)

        return dp[-1]

    # Dp + binary search
    def jobScheduling2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = []
        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[1])

        nums = sorted([0] + endTime)

        def helper(target):

            left = 0
            right = n
            res = 0
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    res = nums[mid]
                    left = mid + 1
                else:
                    right = mid - 1

            return dp[res]

        # def helper(target):
        #     index = bisect.bisect_left(nums, target) - 1
        #     return dp[nums[index]]

        dp = defaultdict(int)
        dp[0] = 0
        res = 0
        for job in jobs:
            dp[job[0]] = max(dp[job[0]], helper(job[0]))
            dp[job[1]] = max(dp[job[1]], dp[job[0]] + job[2], helper(job[1]))
            res = max(res, dp[job[1]])

        return res

    def jobScheduling3(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = []
        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[1])
        dp = [0] * (n + 1)

        def helper(index):
            left = 0
            right = index - 1
            res = 0
            while left <= right:
                mid = (left + right) // 2
                if jobs[mid][1] <= jobs[index][0]:
                    res = dp[mid + 1]
                    left = mid + 1
                else:
                    right = mid - 1

            return res

        for i, job in enumerate(jobs):
            preMax = helper(i)
            dp[i + 1] = max(dp[i], preMax + job[2])

        return dp[n]


if __name__ == '__main__':
    s = Solution()
    test1 = [1,2,3,4,6]
    test2 = [3,5,10,6,9]
    test3 = [20,20,100,70,60]
    # test1 = [4,2,4,8,2]
    # test2 = [5,5,5,10,8]
    # test3 = [1,2,8,10,4]
    # test1 = [6,15,7,11,1,3,16,2]
    # test2 = [19,18,19,16,10,8,19,8]
    # test3 = [2,9,1,19,5,7,3,19]
    print(s.jobScheduling3(test1, test2, test3))