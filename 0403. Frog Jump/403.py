from collections import deque
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {}
        for x in stones:
            dp[x] = set()
        dp[0] = {0}

        for x in stones:
            for k in dp[x]:
                for nxt in [k - 1, k, k + 1]:
                    if x + nxt > x and x + nxt in dp:
                        dp[x + nxt].add(nxt)

        return len(dp[stones[-1]]) != 0

    # Online solution. DP
    def canCross2(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True

        for i in range(n):
            for j in range(i - 1, -1, -1):
                step = stones[i] - stones[j]
                if step > j + 1:
                    break
                # if step + 1 < n:
                #     dp[i][step] = dp[i][step] or dp[j][step + 1]
                # if 1 <= step - 1 < n:
                #     dp[i][step] = dp[i][step] or dp[j][step - 1]
                # if 1 <= step < n:
                #     dp[i][step] = dp[i][step] or dp[j][step]
                dp[i][step] = dp[j][step-1] or dp[j][step] or dp[j][step+1]
                if i == n - 1 and dp[i][step]:
                    return True

        return False

    # DFS + memory
    def canCross3(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[-1] * n for _ in range(n)]
        dic = {}
        for i, x in enumerate(stones):
            dic[x] = i

        def helper(i, j):
            if i == n - 1:
                return True

            if dp[i][j] != -1:
                return dp[i][j]

            res = False
            for k in [j - 1, j, j + 1]:
                if k >= 1:
                    if stones[i] + k in dic:
                        res = res or helper(dic[stones[i] + k], k)

            dp[i][j] = res
            return res

        return helper(0, 0)

    # Based on online solution. DFS + memory
    def canCross(self, stones: List[int]) -> bool:
        stones_set = set(stones)
        visited = set()
        queue = deque([(0, 0)])

        while queue:
            stone, step = queue.popleft()
            for k in [step - 1, step, step + 1]:
                if k >= 1 and stone + k in stones_set and (stone + k, k) not in visited:
                    if stone + k == stones[-1]:
                        return True
                    queue.append((stone + k, k))
                    visited.add((stone + k, k))

        return False


if __name__ == '__main__':
    s = Solution()
    test = [0, 1, 3, 5, 6, 8, 12, 17]
    # test = [0,2]
    print(s.canCross(test))
