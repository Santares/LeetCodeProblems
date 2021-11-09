from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def helper(p ,q):
            if p is not None and q is not None:
                return p.val == q.val and helper(p.left, q.right) and helper(p.right, q.left)
            if p or q:
                return False
            return True

        return helper(root.left, root.right)

    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:

        def helper(p, q):
            if p is not None and q is not None:
                return p.val == q.val and helper(p.left, q.right) and helper(p.right, q.left)
            if p or q:
                return False
            return True

        return helper(root, root)