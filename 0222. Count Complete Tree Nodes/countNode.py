from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # Based on online solution. O(logn * logn)
    def countNodes2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left, right = root.left, root.right
        level = 1
        while left and right:
            level += 1
            left = left.left
            right = right.right
        if not left and not right:
            return 2 ** level - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

