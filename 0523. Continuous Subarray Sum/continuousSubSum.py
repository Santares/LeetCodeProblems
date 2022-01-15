from typing import List

class Solution:
    # too slow
    def checkSubarraySum0(self, nums: List[int], k: int) -> bool:
        dic = {0: 0}
        for i, x in enumerate(nums):
            dic[i + 1] = x + dic[i]

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if dic[j + 1] - dic[i] == 0:
                    return True
                elif (dic[j + 1] - dic[i]) % k == 0:
                    return True

        return False


    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        total = 0
        for i, x in enumerate(nums):
            total += x
            newRes = total % k
            if newRes in dic:
                if i > dic[newRes] + 1:
                    return True
            else:
                dic[newRes] = i

        return False