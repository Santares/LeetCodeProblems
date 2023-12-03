from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False
        target = s // k
        nums.sort(reverse=True)
        used = [False] * len(nums)

        def helper(curSum, curIndex, total, count):
            if count == k:
                return True

            if curSum == target:
                return helper(0, 0, total+curSum, count+1)

            for i in range(curIndex, len(nums)):
                if used[i] or nums[i] + curSum > target:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                if nums[i] != -1 and nums[i] + curSum <= target:
                    used[i] = True
                    if helper(curSum + nums[i], i+1, total, count):
                        return True
                    used[i] = False
            return False


        if helper(0, 0, 0, 0):
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    test1 = [815,625,3889,4471,60,494,944,1118,4623,497,771,679,1240,202,601,883]
    test2 = 3
    print(s.canPartitionKSubsets(test1, test2))
