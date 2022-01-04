import random
from typing import List


class Solution:
    origin = []
    dic = {}

    def __init__(self, nums: List[int]):
        self.origin = nums
        for i, x in enumerate(nums):
            self.dic[i] = x

    def reset(self) -> List[int]:
        return self.origin

    def shuffle(self) -> List[int]:
        shuffled = list(self.origin)
        random.shuffle(shuffled)
        return shuffled

# online solution
class Solution2:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        return sorted(self.nums, key=lambda x: random.random())

# online solution
class Solution3:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        return random.sample(self.nums, len(self.nums))

# online solution
class Solution4:
    def __init__(self, nums):
        self.nums = nums[:]
        self.copy = nums[:]

    def reset(self):
        self.nums = self.copy[:]
        return self.nums

    def shuffle(self):
        n = len(self.nums)
        for i in range(n):
            j = random.randint(i, n - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

from itertools import permutations
# online solution
class Solution5:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.permutations = permutations(nums)

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        res = next(self.permutations, None)
        if res == None:
            self.permutations = permutations(self.nums)
            res = next(self.permutations)
        return res