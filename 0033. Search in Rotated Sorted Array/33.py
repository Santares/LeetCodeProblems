from typing import List


class Solution:
    # not O(logn)
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        dic = {}
        for x in nums:
            dic[x] = i
            i += 1
        if target in dic:
            return dic[target]
        return -1

    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search2(self, nums: List[int], target: int) -> int:
        if len(nums) > 1:
            left = 0
            right = len(nums) - 1
            pivot = 0
            while left <= right:
                mid = (left + right) // 2
                if mid - 1 > 0 and nums[mid - 1] > nums[mid]:
                    pivot = mid
                    break
                elif mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                    pivot = mid + 1
                    break
                elif nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            orders = [x for x in range(len(nums))]
            snums = nums[pivot:] + nums[:pivot]
            orders = orders[pivot:] + orders[:pivot]
            index = self.binary_search(snums, target)
            if index == -1:
                return -1
            else:
                return orders[index]

        else:
            if nums[0] == target:
                return 0
            else:
                return -1

    # online soution
    def search3(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

if __name__ == '__main__':
    s = Solution()
    test = [1,3]
    target = 0
    print(s.search2(test, target))