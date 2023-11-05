class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

    def hammingWeight2(self, n: int) -> int:
        res = 0
        while n:
            if n & 1:
                res += 1
            n = n >> 1

        return res

    # online solution
    def hammingWeight3(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= n - 1
        return count

    # 20231103
    def hammingWeight4(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n // 2
        return res
