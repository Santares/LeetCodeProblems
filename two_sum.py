from typing import List


def twoSum1(self, nums: List[int], target: int) -> List[int]:
    length = len(nums)
    i = 0
    while i < length:
        j = i + 1
        while j < length:
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        i += 1
    return []


def twoSum2(self, nums: List[int], target: int) -> List[int]:
    i = 0
    temp_dic = {}
    for x in nums:
        temp_dic[x] = i
        i += 1
    i = 0
    for x in nums:
        if (target - x) in temp_dic and temp_dic[(target -x)] != i:
            return [i, temp_dic[target - x]]
        i += 1
    return []


