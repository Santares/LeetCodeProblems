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

    # Based on online solution. Two pointers + graph
    def findDuplicate4(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

    # Based on online solution, bit manipulation
    def findDuplicate5(self, nums: List[int]) -> int:
        bitNum = 0
        n = len(nums) - 1
        while n:
            bitNum += 1
            n = n // 2

        res = 0

        for i in range(bitNum + 1):
            x = 0
            y = 0
            for j in range(len(nums)):
                if j & (1 << i):
                    x += 1
                if nums[j] & (1 << i):
                    y += 1
            if y > x:
                # res = res | (1 << i)
                res = res + (1 << i)

        return res

    # Based on online solution, binary search
    def findDuplicate6(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        res = 0
        while left <= right:
            m = (left + right) // 2

            count = 0
            for i in range(n):
                if nums[i] <= m:
                    count += 1

            if count <= m:
                left = m + 1
            else:
                right = m - 1
                res = m

        return res