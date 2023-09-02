from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        visitedStarts = set()

        def helper(i, cur):
            if i >= len(nums):
                if len(cur) >= 2:
                    res.append(list(cur))
                return

            visited = set()
            for j in range(i, len(nums)):
                if cur:
                    if nums[j] >= cur[-1] and nums[j] not in visited:
                        cur.append(nums[j])
                        helper(j + 1, cur)
                        cur.pop()
                        visited.add(nums[j])
                else:
                    if nums[j] in visitedStarts:
                        continue
                    visited.add(nums[j])
                    visitedStarts.add(nums[j])
                    cur.append(nums[j])
                    helper(j + 1, cur)
                    cur.pop()

            if len(cur) >= 2:
                res.append(list(cur))

        helper(0, [])

        return res

    # Simplified version of solution 1
    def findSubsequences2(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(i, cur):
            if len(cur) >= 2:
                res.append(list(cur))

            visited = set()
            for j in range(i, len(nums)):
                if (not cur or nums[j] >= cur[-1]) and nums[j] not in visited:
                    cur.append(nums[j])
                    helper(j + 1, cur)
                    cur.pop()
                    visited.add(nums[j])

        helper(0, [])

        return res
