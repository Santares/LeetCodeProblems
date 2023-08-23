from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        dic = {}
        for k, x in enumerate(nums):
            if x in dic:
                dic[x].append(k)
            else:
                dic[x] = [k]

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                total = nums[i] + nums[j]
                target = 0 - total
                if target in dic:
                    for y in dic[target]:
                        if y > j:
                            temp = tuple([nums[i], nums[j], target])
                            if temp not in res:
                                res.add(temp)
                            break

        return res

    # 2023/08/22
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        dic = {}
        for i, x in enumerate(nums):
            dic[x] = i

        res = set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                target = 0 - nums[i] - nums[j]
                if target in dic and dic[target] > j:
                    temp = tuple([nums[i], nums[j], target])
                    if temp not in res:
                        res.add(temp)
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        length = len(nums)
        i = 0

        while i < length - 2 and nums[i] <= 0:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            left = i + 1
            right = length - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
            i += 1

        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0,0,0]
    # nums = [0,1,1]
    print(solution.threeSum3(nums))
