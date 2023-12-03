from collections import Counter


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        sCount = Counter(corridor)['S']
        if sCount % 2 != 0 or sCount == 0:
            return 0

        res = 0
        count = 0
        ways = []
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                if count == 2:
                    res += 1
                    ways.append(res)
                    res = 0
                    count = 1
                else:
                    count += 1
            else:
                if count == 2:
                    res += 1

        mod = (10 ** 9 + 7)
        res = 1
        for x in ways:
            res = res * x % mod

        return res