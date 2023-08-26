# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        stack = [root]
        res = []
        while stack:
            head = stack.pop()
            res.append(head.val)
            if head.left:
                stack.append(head.left)
            if head.right:
                stack.append(head.right)

        return res[::-1]
