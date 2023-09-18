from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # DFS
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        if p is None and q is None:
            return True

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # 2023/09/18. BFS
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 and queue2:
            if len(queue1) != len(queue2):
                return False
            for _ in range(len(queue1)):
                p, q = queue1.popleft(), queue2.popleft()
                if (not p and q) or (p and not q):
                    return False
                if not p and not q:
                    continue

                if p.val != q.val:
                    return False

                queue1 += [p.left, p.right]
                queue2 += [q.left, q.right]

        if queue1 or queue2:
            return False
        else:
            return True
