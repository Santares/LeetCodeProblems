from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left is None and root.right:
            return self.minDepth(root.right) + 1
        elif root.left and root.right is None:
            return self.minDepth(root.left) + 1
        else:
            return 1

    # bfs, fast
    def minDepth2(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = []
        queue.append(root)
        level = 1
        while queue:
            temp = []
            for node in queue:
                if node.left is None and node.right is None:
                    return level
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level += 1
            queue = temp