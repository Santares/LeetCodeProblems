class Solution:
    # Online solution
    def countOrders(self, n: int) -> int:
        res = 1
        mod = 10 ** 9 + 7
        for i in range(2, n + 1):
            res = res * (2 * i - 1) * i % mod

        return res
