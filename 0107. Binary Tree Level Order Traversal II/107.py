# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        res = []
        while queue:
            cur = []
            nxt = []
            for node in queue:
                cur.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            queue = nxt
            res.append(cur)
        return res[::-1]

    def levelOrderBottom2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stack = [[root]]
        res = []

        queue = deque()
        queue.append(root)
        while queue:
            l = len(queue)
            cur = []
            for _ in range(l):
                node = queue.popleft()
                if node.left:
                    cur.append(node.left)
                    queue.append(node.left)
                if node.right:
                    cur.append(node.right)
                    queue.append(node.right)
            if cur:
                stack.append(cur)

        while stack:
            cur = stack.pop()
            tmp = []
            for node in cur:
                tmp.append(node.val)
            res.append(tmp)

        return res
