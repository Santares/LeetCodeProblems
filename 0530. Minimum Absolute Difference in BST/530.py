# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Based on online solution. Save space
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.last = None
        self.res = float('inf')

        def helper(root):
            if root.left:
                helper(root.left)

            if self.last:
                self.res = min(self.res, abs(self.last.val - root.val))
            self.last = root

            if root.right:
                helper(root.right)

        helper(root)

        return self.res
