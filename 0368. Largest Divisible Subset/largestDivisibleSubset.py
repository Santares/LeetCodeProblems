from typing import List

class Solution:
    # slow
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        def helper(current, nums):
            if not nums:
                if not current:
                    return []
                return current

            x = nums[0]
            if current:
                for y in current:
                    if y % x != 0 and x % y != 0:
                        return helper(current, nums[1:])
            else:
                current = []

            first = helper(current + [x], nums[1:])
            second = helper(current, nums[1:])

            if len(first) < len(second):
                return second
            return first

        return helper([], nums)

    # acceptable, slow
    def largestDivisibleSubset2(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums = sorted(nums)

        @cache
        def helper(last, i):
            if i >= l:
                return []

            x = nums[i]
            if last != 0:
                if last % x != 0 and x % last != 0:
                    return helper(last, i+1)

            first = helper(x, i + 1)
            second = helper(last, i + 1)

            if len(first) + 1 < len(second):
                return second
            return [x] + first

        return helper(0, 0)




if __name__ == '__main__':
    solution = Solution()
    test = [5,9,18,54,108,540,90,180,360,720]
    print(solution.largestDivisibleSubset2(test))