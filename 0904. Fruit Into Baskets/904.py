from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        left = 0
        basket = {}

        for right in range(len(fruits)):
            if fruits[right] in basket:
                basket[fruits[right]] += 1
            else:
                if len(basket) <= 1:
                    basket[fruits[right]] = 1
                else:
                    while True:
                        basket[fruits[left]] -= 1
                        left += 1
                        if basket[fruits[left - 1]] == 0:
                            del basket[fruits[left - 1]]
                            break
                    basket[fruits[right]] = 1
            res = max(res, right - left + 1)

        return res

    # Online solution
    def totalFruit2(self, fruits: List[int]) -> int:
        l, r, total, results = 0, 0, 0, 0
        count = defaultdict(int)

        for r in range(len(fruits)):
            count[fruits[r]] += 1

            if len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
        return r - l + 1


if __name__ == '__main__':
    s = Solution()
    test = [3,3,3,1,2,1,1,2,3,3,4]
    test = [1,1,2,3]
    print(s.totalFruit2(test))