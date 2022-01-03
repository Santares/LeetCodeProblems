from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, x in enumerate(nums):
            if x not in dic:
                dic[x] = i
            else:
                if i - dic[x] <= k:
                    return True
                else:
                    dic[x] = i
        return False