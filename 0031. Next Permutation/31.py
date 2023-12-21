from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        n = len(nums)
        index = n-1
        while index >= 0:
            if index < n-1 and nums[index] < nums[index+1]:
                j = index + 1
                while j < n-1 and nums[j+1] > nums[index]:
                    j += 1
                nums[index], nums[j] = nums[j], nums[index]
                l = index + 1
                r = n-1
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                return
            else:
                index -= 1

        nums.reverse()
        return

    # based on online solution
    def nextPermutation2(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        l = i + 1
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return


if __name__ == '__main__':
    s = Solution()
    test1 = [1,2,3]
    print(s.nextPermutation(test1))