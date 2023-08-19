from collections import deque


class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = deque()
        for c in s:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)

        return ''.join(res)

    def removeDuplicates2(self, s: str) -> str:
        res = []
        for c in s:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)

        return ''.join(res)
