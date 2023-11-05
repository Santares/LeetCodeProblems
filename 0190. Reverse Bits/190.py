class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        b = b[::-1] + (32 - len(b)) * "0"
        return int(b, 2)

    def reverseBits2(self, n: int) -> int:
        l = ""
        while n:
            l += str(n % 2)
            n = n // 2

        l += (32 - len(l)) * "0"
        return int(l, 2)