from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def goDeep(nums, root):
            if root is None:
                return 0
            nums.append(root.val)
            if root.left is None and root.right is None:
                res = 0
                size = len(nums)
                for i, v in enumerate(nums):
                    res += v * 10 ** (size - i - 1)
                return res
            else:
                return goDeep(list(nums), root.left) + goDeep(list(nums), root.right)

        return goDeep([], root)

    # online solution, not faster
    def sumNumbers2(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def helper(root, curr):
            if root:
                if not root.left and not root.right:
                    self.ans += 10 * curr + root.val
                helper(root.left, 10 * curr + root.val)
                helper(root.right, 10 * curr + root.val)

        helper(root, 0)
        return self.ans