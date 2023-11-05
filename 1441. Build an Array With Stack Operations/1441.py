from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i = 0
        j = 1
        while i < len(target):
            while j < target[i]:
                res += ["Push", "Pop"]
                j += 1
            res.append("Push")
            i += 1
            j += 1
        return res