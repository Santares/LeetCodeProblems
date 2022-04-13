from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tmp = set()
        res = []
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
                            tmp.add(str(nums[i]) + ',' + str(nums[j]) + ',' + str(target))
                            break
                else:
                    continue
        for s in tmp:
            res.append(s.split())
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(solution.threeSum(nums))