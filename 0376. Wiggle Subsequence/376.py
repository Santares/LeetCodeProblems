from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res = 1
        last = nums[0]
        lastSign = 0 # 1: pos, -1: neg, 0: init
        for x in nums[1:]:
            if x-last > 0:
                if lastSign != 1:
                    last = x
                    res += 1
                    lastSign = 1
                elif x > last:
                    last = x
            elif x-last < 0:
                if lastSign != -1:
                    last = x
                    res += 1
                    lastSign = -1
                elif x < last:
                    last = x

        return res