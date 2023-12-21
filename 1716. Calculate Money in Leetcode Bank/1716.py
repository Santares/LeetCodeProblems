class Solution:
    def totalMoney(self, n: int) -> int:
        x = n // 7
        y = n % 7
        res = 0

        res += (1 + y) * y // 2 + y * x

        while x > 0:
            x -= 1
            res += 28 + 7 * x

        return res
