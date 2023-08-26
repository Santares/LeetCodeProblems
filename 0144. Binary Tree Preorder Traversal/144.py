# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(root):
            if not root:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
            return

        helper(root)
        return res

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        queue = [root]
        res = []
        while queue:
            head = queue.pop()
            res.append(head.val)
            if head.right:
                queue.append(head.right)
            if head.left:
                queue.append(head.left)

        return res
