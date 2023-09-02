from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def helper(i, cur, total):
            if len(cur) == k-1 and cur:
                if cur[-1] < n - total < 10:
                    res.append(cur+[n-total])

                return

            for x in range(i, 10):
                cur.append(x)
                total += x
                helper(x + 1, cur, total)
                cur.pop()
                total -= x

        helper(1, [], 0)

        return res