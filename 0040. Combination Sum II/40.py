from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def helper(i, cur, target):
            if target == 0:
                res.append(list(cur))
                return
            for j in range(i, len(candidates)):
                if target < candidates[j]:
                    return
                elif j > i and candidates[j] == candidates[j - 1]:
                    continue
                else:
                    cur.append(candidates[j])
                    helper(j + 1, cur, target - candidates[j])
                    cur.pop()

            return

        helper(0, [], target)

        return res
