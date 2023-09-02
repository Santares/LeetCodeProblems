from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for x in nums:
            for i in range(len(subset)):
                subset.append(subset[i] + [x])

        return subset

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]
        return output

    # backtracing
    def subsets3(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output

    # binary bit mask
    def subsets4(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output

    # 2023/09/01, back tracing
    def subsets5(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(i, cur):
            if i >= n:
                res.append(list(cur))
                return

            for j in range(i, n):
                cur.append(nums[j])
                helper(j + 1, cur)
                cur.pop()
            res.append(list(cur))

        helper(0, [])

        return res