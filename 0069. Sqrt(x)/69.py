class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            value = mid * mid
            if value < x:
                left = mid + 1
            elif value == x:
                return mid
            else:
                right = mid - 1
        return right