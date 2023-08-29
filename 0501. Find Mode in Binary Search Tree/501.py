# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Based on online solution. Save space
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.maxCount = 0
        self.res = []
        self.count = 0
        self.last = None

        def helper(root):
            if root.left:
                helper(root.left)

            if self.last and root.val == self.last.val:
                self.count += 1
            else:
                self.count = 1

            if self.count == self.maxCount:
                self.res.append(root.val)
            elif self.count > self.maxCount:
                self.res = [root.val]
                self.maxCount = self.count

            self.last = root

            if root.right:
                helper(root.right)

        helper(root)
        return self.res
