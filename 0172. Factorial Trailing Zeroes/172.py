class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        m = 5
        while m <= n:
            res += n // m
            m *= 5

        return res

