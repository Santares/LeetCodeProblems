from typing import List


class Solution:
    # fast, but not O(n)
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        x = 1
        for i in nums:
            if x < i:
                return x
            elif x == i:
                x += 1

        return x

    # slower, space not O(1)
    def firstMissingPositive2(self, nums: List[int]) -> int:
        l = len(nums)
        temp = [1] * l

        for i in nums:
            if i > 0 and i <= l:
                temp[i - 1] = 0

        for i in range(l):
            if temp[i] == 1:
                return i + 1

        return l + 1

    # online solution, O(n) + O(1), slow
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
         the range [1,...,l+1] 
    """
    def firstMissingPositive3(self, nums):
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):
            if nums[i]//n==0:
                return i
        return n

    # online solution, O(n) + O(1), slow
    def firstMissingPositive4(self, nums):
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1