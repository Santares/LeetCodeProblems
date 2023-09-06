# Definition for a binary tree node.
from functools import cache
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def helper(root, parentRobbed):
            if not root:
                return 0

            a = helper(root.left, True) + helper(root.right, True) + root.val
            b = helper(root.left, False) + helper(root.right, False)

            if parentRobbed:
                return b
            else:
                return max(a, b)

        return helper(root, False)

    def rob2(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if not root:
                return [0, 0]

            left = helper(root.left)
            right = helper(root.right)

            a = root.val + left[1] + right[1]
            b = max(left) + max(right)

            # [rob current, don't rob current]
            return [a, b]

        r = helper(root)
        return max(r)


if __name__ == '__main__':
    s = Solution()
    test = TreeNode(3, TreeNode(4,TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
    print(s.rob2(test))