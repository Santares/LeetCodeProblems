from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l):
            for j in range(i, l):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]


    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
                j += 1
            else:
                j += 1

if __name__ == '__main__':
    solution = Solution()
    test = [2,0,2,1,1,0]
    test = [2,0,1]
    solution.sortColors2(test)
    print(test)