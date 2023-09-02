from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(candidates, cur):
            if not candidates:
                res.append(cur.copy())
                return

            for i in range(len(candidates)):
                cur.append(candidates[i])
                helper(candidates[:i] + candidates[i + 1:], cur)
                cur.pop()

        helper(nums, [])

        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(cur, used):
            if len(cur) == n:
                res.append(cur.copy())
                return

            for x in nums:
                if x not in used:
                    used.add(x)
                    cur.append(x)
                    helper(cur, used.copy())
                    cur.pop()
                    used.remove(x)

        helper([], set())

        return res