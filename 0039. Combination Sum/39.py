from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def helper(i, cur, target):
            if target == 0:
                res.append(list(cur))
                return
            for j in range(i, len(candidates)):
                if target < candidates[j]:
                    return
                else:
                    cur.append(candidates[j])
                    helper(j, cur, target - candidates[j])
                    cur.pop()

            return

        helper(0, [], target)

        return res
