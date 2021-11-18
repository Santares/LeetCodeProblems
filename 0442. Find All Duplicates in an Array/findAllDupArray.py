from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = {}
        res = []
        for i in nums:
            if i in dic:
                res.append(i)
            dic[i] = 0

        return res

    # a little slower
    def findDuplicates2(self, nums: List[int]) -> List[int]:
        dic = [0] * len(nums)
        res = []
        for i in nums:
            if dic[i - 1] == 1:
                res.append(i)
            else:
                dic[i - 1] = 1

        return res