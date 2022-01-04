class Solution:
    def bitwiseComplement(self, n: int) -> int:
        l = len(bin(n)) - 2
        return n ^ (2 ** l - 1)

    # online solution
    def bitwiseComplement2(self, n: int) -> int:
        X = 1
        while n > X: X = X * 2 + 1
        return X - n