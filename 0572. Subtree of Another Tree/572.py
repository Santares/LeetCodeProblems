# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSame(self, r, s):
        if not r and not s:
            return True
        if r and s and r.val == s.val:
            return self.isSame(r.left, s.left) and self.isSame(r.right, s.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif root and subRoot:
            return self.isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,
                                                                                                      subRoot)
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    test1 = TreeNode(1, TreeNode(2, TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(3))), TreeNode(3))
    test2 = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(3))
    print(s.isSubtree(test1, test2))
