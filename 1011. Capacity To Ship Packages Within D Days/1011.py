from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        low = total // days
        high = total

        def helper(cap):
            need = 1
            cum = 0
            for x in weights:
                if x > cap:
                    return False
                cum += x
                if cum > cap:
                    need += 1
                    cum = x
            return need <= days

        while low <= high:
            mid = low + (high - low) // 2
            if helper(mid):
                high = mid - 1
            else:
                low = mid + 1

        return high + 1


if __name__ == '__main__':
    s = Solution()
    test1 = [1, 2, 3, 1, 1]
    test2 = 4

    print(s.shipWithinDays(test1, test2))
