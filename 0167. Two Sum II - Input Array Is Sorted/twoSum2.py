from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i


    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while True:
            s = numbers[left] + numbers[right]

            if s == target:
                return [left + 1, right + 1]
            elif s > target:
                right -= 1
            else:
                left += 1

    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, x in enumerate(numbers):
            dic[x] = i
        i = 0
        for x in numbers:
            if target - x in dic and dic[target-x] != i:
                return [i+1, dic[target-x]+1]
            i += 1