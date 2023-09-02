from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def isValid(ns):
            if len(ns) > 1 and ns[0] == '0':
                return False
            ns = int(''.join(ns))
            if ns > 255:
                return False
            return True

        def helper(i, start, cur):
            if len(cur) == 4:
                if start >= n:
                    res.append('.'.join(cur))
                return
            for j in range(i, n):
                ns = s[start:j + 1]
                if isValid(ns):
                    cur.append(ns)
                    helper(j + 1, j + 1, cur)
                    cur.pop()

        helper(0, 0, [])

        return res

