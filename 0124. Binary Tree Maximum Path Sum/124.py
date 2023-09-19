# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')

        def helper(root):
            if not root:
                return 0

            left = max(helper(root.left), 0)
            right = max(helper(root.right), 0)

            cur = left + root.val + right
            self.res = max(self.res, cur)

            return root.val + max(left, right)

        helper(root)

        return self.res
