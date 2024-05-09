# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        def helper(root):
            if not root:
                return
            helper(root.left)
            if low <= root.val <= high:
                self.res += root.val
            helper(root.right)

        helper(root)
        return self.res
