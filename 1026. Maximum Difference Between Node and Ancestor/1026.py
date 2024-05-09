# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root, maxV, minV):
            if not root:
                return maxV - minV
            v = root.val
            if maxV == -1 or v > maxV:
                maxV = v
            if minV == -1 or v < minV:
                minV = v
            return max(helper(root.left, maxV, minV), helper(root.right, maxV, minV))

        return helper(root, -1, -1)
