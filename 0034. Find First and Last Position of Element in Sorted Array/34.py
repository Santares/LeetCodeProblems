from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if mid - 1 >= 0 and nums[mid-1] == target:
                    right = mid - 1
                else:
                    start = mid
                    break

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if mid + 1 < len(nums) and nums[mid + 1] == target:
                    left = mid + 1
                else:
                    end = mid
                    break

        return [start, end]

    # online solution
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        def binSearch(leftMost: bool) -> int:
            low, high, result = 0, len(nums) - 1, -1

            # Repeat until the pointers low and high meet each other
            while low <= high:
                mid = (low + high) // 2  # middle index - divide & conquer
                if target == nums[mid]:  # target found
                    result = mid
                    if leftMost:
                        high = mid - 1  # continue search for leftMost
                    else:
                        low = mid + 1  # continue search for rightMost
                elif target > nums[mid]:
                    low = mid + 1  # target is on the right side
                else:
                    high = mid - 1  # target is on the left side

            return result

        return (binSearch(True), binSearch(False))  # Time Complexity logN+logN = 2 logN = logN

    # improved version of solution 1
    def searchRange3(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                start = mid
                right = mid - 1

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                end = mid
                left = mid + 1

        return [start, end]



if __name__ == '__main__':
    s = Solution()
    test = [5,7,7,8,8,10]
    target = 8
    print(s.searchRange(test, target))

