# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res = []

        def helper(node, cur):
            cur.append(node)
            if not node.left and not node.right:
                path = "->".join([str(node.val) for node in cur])
                res.append(path)
                return
            if node.left:
                helper(node.left, list(cur))
            if node.right:
                helper(node.right, list(cur))

        helper(root, [])
        return res
