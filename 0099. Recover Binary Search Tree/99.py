# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = [None, None, None]

        def traverse(root):
            if not root:
                return

            traverse(root.left)

            if nodes[2] and root.val < nodes[2].val:
                if not nodes[0]:
                    nodes[0] = nodes[2]
                    nodes[1] = root
                else:
                    nodes[1] = root
                    return
            nodes[2] = root

            traverse(root.right)

        traverse(root)

        nodes[0].val, nodes[1].val = nodes[1].val, nodes[0].val
