from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        nonZeroProd = 0
        res = []
        zeros = 0
        for x in nums:
            if zeros > 1:
                nonZeroProd = 0
                break
            if x:
                if nonZeroProd:
                    nonZeroProd *= x
                else:
                    nonZeroProd = x
            else:
                zeros += 1

            prod = prod * x

        if zeros > 1:
            nonZeroProd = 0

        for x in nums:
            if x:
                res.append(prod // x)
            else:
                res.append(nonZeroProd)

        return res

    # online solution, slower
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        maxProduct = 1
        for num in nums:
            if num != 0:
                maxProduct *= num

        zeroCount = nums.count(0)
        if not zeroCount:
            return [maxProduct // x for x in nums]
        elif zeroCount == 1:
            return [0 if x != 0 else maxProduct for x in nums]
        else:
            return [0] * len(nums)