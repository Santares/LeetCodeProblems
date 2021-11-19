from itertools import zip_longest
from typing import List


class Solution:
    # too slow
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0

        l = len(nums)
        for i in range(l):
            for j in range(i + 1, l):
                res += bin(nums[i] ^ nums[j]).count('1')

        return res

    # faster
    def totalHammingDistance2(self, nums: List[int]) -> int:
        temp = []
        l = 0
        for x in nums:
            s = bin(x)
            l = max(l, len(s))
            temp.append(s[2:])

        l -= 2

        newTemp = []
        for s in temp:
            newTemp.append('0' * (l - len(s)) + s)

        res = 0
        for i in range(l):
            ones = 0
            zeros = 0
            for s in newTemp:
                if s[i] == '0':
                    zeros += 1
                else:
                    ones += 1
            res += ones * zeros

        return res

    # online solution, use zip, faster
    def totalHammingDistance3(self, nums: List[int]) -> int:
        res = 0
        temp = [bin(x)[-1:1:-1] for x in nums]

        for value in zip_longest(*temp, fillvalue='0'):
            ones = value.count('1')
            zeros = len(value) - ones
            res += ones * zeros

        return res


if __name__ == '__main__':
    s = Solution()
    test = [4, 14, 2]
    print(s.totalHammingDistance3(test))
