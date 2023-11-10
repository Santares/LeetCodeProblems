from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for x, f in count.items():
            if f == 1:
                return x

    # Online solution, bit manipulation
    def singleNumber2(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans


if __name__ == '__main__':
    s = Solution()
    test = [2,2,3,2]
    print(s.singleNumber2(test))
