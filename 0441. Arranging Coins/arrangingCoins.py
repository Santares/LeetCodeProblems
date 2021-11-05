class Solution:
    # slow
    def arrangeCoins(self, n: int) -> int:
        i = 0
        while(True):
            x =  (1 + i ) * i /2
            if x > n:
                return i - 1
            i += 1

    # a little faster
    def arrangeCoins2(self, n: int) -> int:
        i = 0
        x = 0
        while(True):
            x += i
            if x > n:
                return i - 1
            i += 1

    # binary search, fast
    def arrangeCoins3(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            mid = (left + right) // 2
            x = (mid + 1) * mid // 2
            if x == n:
                return mid
            elif x < n:
                left = mid + 1
            else:
                right = mid - 1

        return right
