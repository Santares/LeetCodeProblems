from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        count = sorted(count.values(), reverse=True)
        last = count[0]
        res = 0
        for x in count[1:]:
            if last == 0:
                res += x
            elif x >= last:
                last -= 1
                res += x - last
            else:
                last = x

        return res
