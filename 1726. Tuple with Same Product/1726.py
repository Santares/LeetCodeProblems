from collections import defaultdict
from typing import List


class Solution:
    # too slow
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        numsDict = {}
        for i, x in enumerate(nums):
            numsDict[x] = i
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                x = nums[i] * nums[j]
                for k, y in enumerate(nums):
                    if k != i and k != j and x % y == 0:
                        z = x // y
                        if z in numsDict and numsDict[z] != i and numsDict[z] != j and numsDict[z] != k:
                            res += 2
        return res

    # Online solution
    def tupleSameProduct2(self, nums: List[int]) -> int:
        product = defaultdict(int)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                product[nums[i] * nums[j]] += 1

        res = 0
        for p, c in product.items():
            res += c * (c - 1) * 4

        return res


if __name__ == '__main__':
    s = Solution()
    test = [2,3,4,6]
    print(s.tupleSameProduct((test)))