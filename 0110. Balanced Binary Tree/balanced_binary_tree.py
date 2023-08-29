from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def calHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if (root.left is not None) and (root.right is not None):
            return max(self.calHeight(root.left), self.calHeight(root.right)) + 1
        elif (root.left is None) and (root.right is not None):
            return self.calHeight(root.right) + 1
        elif (root.left is not None) and (root.right is None):
            return self.calHeight(root.left) + 1
        else:
            return 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        lh = 0
        rh = 0
        if root is None:
            return True

        if root.left is not None:
            lh = self.calHeight(root.left)

        if root.right is not None:
            rh = self.calHeight(root.right)

        if abs(rh - lh) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    # online solution + own solution => improved solution
    def isBalanced2(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.calHeight2(root) != -1

    def calHeight2(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        lh = self.calHeight2(root.left)
        rh = self.calHeight2(root.right)

        if abs(lh - rh) > 1 or lh == -1 or rh == -1:
            return -1

        return max(lh, rh) + 1

    # 2023/08/28
    def isBalanced3(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.res = True

        def helper(root):
            if not root:
                return 0
            else:
                left = helper(root.left)
                right = helper(root.right)
                if abs(left - right) > 1:
                    self.res = False
                return max(left, right) + 1

        helper(root)
        return self.res
