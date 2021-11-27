from typing import List


class Solution:
    # slow
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = set()
        for x in nums:
            if x in record:
                return True
            else:
                record.add(x)

        return False
