class Solution:
    def maxDepth(self, s: str) -> int:
        stack = 0
        res = 0
        for c in s:
            if c == '(':
                stack += 1
                res = max(res, stack)
            if c == ')':
                stack -= 1

        return res