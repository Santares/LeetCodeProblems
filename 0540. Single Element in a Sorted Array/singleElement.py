from typing import List


class Solution:
    # slow
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        l = len(nums)
        right = l
        while True:
            i = (right + left) // 2
            if i == (l - 1) or i == 0:
                return nums[i]
            if nums[i] != nums[i + 1] and nums[i] != nums[i - 1]:
                return nums[i]

            if i % 2 == 0:
                if nums[i] != nums[i + 1]:
                    right = i
                else:
                    left = i
            else:
                if nums[i] != nums[i - 1]:
                    right = i
                else:
                    left = i

    # a little faster
    def singleNonDuplicate2(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(0, l, 2):
            if i + 1 == l or nums[i] != nums[i + 1]:
                return nums[i]

    # online solution, not faster
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if r == 1:
            return nums[0]

        while True:
            if l == r:
                return nums[l]

            m = (l + r) // 2
            if m % 2 == 0:
                if nums[m] == nums[m - 1]:
                    r = m
                elif nums[m] == nums[m + 1]:
                    l = m + 1
                else:
                    return nums[m]
            else:
                if nums[m] == nums[m - 1]:
                    l = m + 1
                elif nums[m] == nums[m + 1]:
                    r = m
                else:
                    return nums[m]

        return 0

if __name__ == '__main__':
    solution = Solution()
    test = [1,1,2]
    print(solution.singleNonDuplicate(test))