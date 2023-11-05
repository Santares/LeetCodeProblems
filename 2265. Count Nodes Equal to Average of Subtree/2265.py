from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def helper(root):
            if not root:
                return 0, 0
            leftTotal, leftCount = helper(root.left)
            rightTotal, rightCount = helper(root.right)
            total = leftTotal + rightTotal + root.val
            totalCount = leftCount + rightCount + 1
            if root.val == total // totalCount:
                self.count += 1
            return total, totalCount

        helper(root)
        return self.count
