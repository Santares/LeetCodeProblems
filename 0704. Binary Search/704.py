from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid - 1

        return -1

    def search1(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid
        if nums[right] == target:
            return right
        else:
            return -1

    def search2(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    test = [1,2,3]
    target = 2
    test = [1, 2, 3]
    target = 1
    test = [-1,0,3,5,9,12]
    target = 2
    test = [-1,0,3,5,9,12]
    target = 13
    print(s.search(test, target))
