from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root

        def invert(root: Optional[TreeNode]):
            if root is not None:
                invert(root.left)
                invert(root.right)
                root.left, root.right = root.right, root.left

        invert(root)
        return root

    # improved, not faster
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left, root.right = right, left

        return root