from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(i, cur):
            if i >= len(nums):
                res.append(list(cur))
                return

            res.append(list(cur))
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                cur.append(nums[j])
                helper(j + 1, cur)
                cur.pop()

        helper(0, [])

        return res

    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(i, cur):
            if i >= len(cur):
                res.append(list(cur))

            visited = set()
            for j in range(i, len(nums)):
                if nums[j] not in visited:
                    cur.append(nums[j])
                    helper(j + 1, cur)
                    cur.pop()
                    visited.add(nums[j])

        helper(0, [])

        return res