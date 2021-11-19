from collections import Counter


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        s = bin(z)[2:]

        res = 0

        for c in s:
            if c == '1':
                res += 1

        return res

    # faster, use Counter
    def hammingDistance2(self, x: int, y: int) -> int:
        s = bin(x ^ y)[2:]

        l = Counter(list(s))

        return l['1']

    # online solution
    def hammingDistance3(self, x: int, y: int) -> int:
        s = bin(x ^ y)

        return s.count('1')


    def hammingDistance4(self, x: int, y: int) -> int:
        z = x ^ y
        res = 0
        while z:
            if z & 1:
                res += 1
            z = z >> 1

        return res
