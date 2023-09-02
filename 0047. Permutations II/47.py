from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(candidates, cur):
            if not candidates:
                res.append(cur.copy())
                return

            used = set()
            for i in range(len(candidates)):
                if candidates[i] not in used:
                    used.add(candidates[i])
                    cur.append(candidates[i])
                    helper(candidates[:i] + candidates[i + 1:], cur)
                    cur.pop()

        helper(nums, [])

        return res

    # Based on online solution
    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        visited = [False] * n

        def helper(i, cur):
            if i >= n:
                res.append(cur.copy())
                return

            for j in range(n):
                if j > 0 and nums[j] == nums[j - 1] and not visited[j - 1]:
                    continue
                if not visited[j]:
                    visited[j] = True
                    cur.append(nums[j])
                    helper(i + 1, cur)
                    cur.pop()
                    visited[j] = False

        helper(0, [])

        return res
