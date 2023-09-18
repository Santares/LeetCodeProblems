# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        if not root.left and not root.right and targetSum == 0:
            return True

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


if __name__ == '__main__':
    s = Solution()
    test1 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))))
    test2 = 22

    test1 = TreeNode(-3, None, TreeNode(-2))
    test2 = -5

    print(s.hasPathSum(test1, test2))
