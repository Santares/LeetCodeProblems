from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:
        new_root = None
        current = new_root

        def helper(root, new_root, current):
            if root is None:
                return new_root, current

            new_root, current = helper(root.left, new_root, current)

            if new_root is None:
                new_root = TreeNode(root.val)
                current = new_root
            else:
                current.right = TreeNode(root.val)
                current = current.right

            return helper(root.right, new_root, current)

        new_root, current = helper(root, new_root, current)

        return new_root

    # online solution
    def increasingBST2(self, root: TreeNode) -> TreeNode:
        lst = []

        def helper(root):
            if root is None:
                return
            helper(root.left)
            lst.append(root.val)
            helper(root.right)

        helper(root)
        new_root = TreeNode(lst[0])
        cur = new_root
        for i in range(1, len(lst)):
            cur.right = TreeNode(lst[i])
            cur = cur.right
        return new_root

