from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = 0

        res = []

        for i in range(1, len(nums) + 1):
            if i not in dic:
                res.append(i)

        return res

    # faster
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        l = len(nums)
        dic = [0] * l
        res = []

        for i in nums:
            dic[i - 1] = 1

        for i in range(l):
            if dic[i] == 0:
                res.append(i + 1)

        return res

    # online solution
    def findDisappearedNumbers3(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        missing = []
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                missing.append(i)
        return missing

    # online solution
    def findDisappearedNumbers4(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)) - set(nums))