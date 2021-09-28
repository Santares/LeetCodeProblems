from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        nodes = []
        current = root
        while i < k:
            while current is not None:
                if current.left is not None:
                    nodes.append(current)
                    current = current.left
                else:
                    i += 1
                    if i == k:
                        return current.val
                    current = current.right
            current = nodes.pop(-1)
            i += 1
            if i == k:
                return current.val
            current = current.right

        return current.val

    # online solution
    def kthSmallest2(self, root, k):
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]

    # online solution
    def kthSmallest3(self, root, k):
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right