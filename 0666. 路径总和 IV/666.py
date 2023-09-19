class Solution:
    def pathSum(self, nums: List[int]) -> int:
        self.res = 0
        values = {x // 10: x % 10 for x in nums}

        def dfs(node, cur):
            if node not in values:
                return

            cur += values[node]
            level = node // 10
            pos = node % 10

            left = (level + 1) * 10 + pos * 2 - 1
            right = left + 1

            if left not in values and right not in values:
                self.res += cur
                return

            dfs(left, cur)
            dfs(right, cur)

            return

        dfs(nums[0] // 10, 0)
        return self.res