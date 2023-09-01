from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(i, cur):
            if len(cur) == k:
                res.append(list(cur))
                return
            for x in range(i, n + 1):
                cur.append(x)
                helper(x + 1, cur)
                cur.pop()

        helper(1, [])

        return res
