from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArithmetic(arr):
            if len(arr) > 2:
                arr.sort()
                dif = arr[1] - arr[0]
                for i in range(2, len(arr)):
                    if arr[i] - arr[i - 1] != dif:
                        return False

            return True

        res = []
        for i in range(len(l)):
            res.append(isArithmetic(nums[l[i]:r[i] + 1]))

        return res