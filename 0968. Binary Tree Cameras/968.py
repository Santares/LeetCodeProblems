# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Online solution, greedy
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # 0: not covered, 1: has camera, 2: covered
        def helper(root):
            if not root:
                return 2

            left = helper(root.left)
            right = helper(root.right)

            if left == right == 1:
                return 2

            if left == right == 2:
                return 0

            if left == 0 or right == 0:
                self.res += 1
                return 1

            return 2

        if helper(root) == 0:
            self.res += 1

        return self.res

    # online solution, dp
    def minCameraCover2(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return float("inf"), 0, 0

            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)

            a = lc + rc + 1
            b = min(a, min(lb + ra, la + rb))
            c = min(a, lb + rb)

            return a, b, c

        a, b, c = dfs(root)
        return b