from typing import List


class Solution:
    # Based on online solution
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def helper(x):
            count = 0
            i = 0
            while i <len(nums)-1:
                if nums[i+1] - nums[i] <= x:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p

        left = 0
        right = nums[-1] - nums[0]
        while left <= right:
            mid = left + (right-left)//2
            if helper(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    s = Solution()
    test = [10,1,2,7,1,3]
    p = 2
    print(s.minimizeMax(test, p))


