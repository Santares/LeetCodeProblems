from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]

    # online solution
    def findDuplicate2(self, nums: List[int]) -> int:

        uniques = set()

        for num in nums:
            if num in uniques:
                return num
            uniques.add(num)

    # online solution
    def findDuplicate3(self, nums: List[int]) -> int:

        d = {}
        for i in nums:
            if i in d:
                return i
            else:
                d[i] = True
