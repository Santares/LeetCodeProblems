from typing import List


class Solution:
    # O(nlogn)
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(set(nums))
        nums.sort()
        count = 1
        res = 1

        last = nums[0]
        for x in nums[1:]:
            if x == last + 1:
                count += 1
                res = max(res, count)
            else:
                count = 1
            last = x

        return res

    # Online solution, O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for x in nums:
            if x - 1 not in nums:
                count = 1
                x += 1
                while x in nums:
                    x += 1
                    count += 1
                res = max(res, count)

        return res

    # Online solution, dp, O(n)
    def longestConsecutive3(self, nums: List[int]) -> int:
        dic = {}
        res = 0

        for x in nums:
            if x not in dic:
                left = dic.get(x - 1, 0)
                right = dic.get(x + 1, 0)
                count = left + right + 1
                dic[x] = -1
                dic[x - left] = count
                dic[x + right] = count
                res = max(res, count)

        return res

    # Online solution, union find
    def longestConsecutive4(self, nums: List[int]) -> int:
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                parent[y] = x
                size[x] += size[y]

        nums = set(nums)
        parent = {num: num for num in nums}
        size = {num: 1 for num in nums}
        res = 0

        for x in nums:
            if x + 1 in nums:
                union(x, x + 1)
            res = max(res, size[find(x)])

        return res