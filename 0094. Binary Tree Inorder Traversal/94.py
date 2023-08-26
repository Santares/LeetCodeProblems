from typing import Optional, List

from utils.tree import TreeNode

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        else:
            return []

    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        queue = [root]
        res = []
        while queue:
            head = queue.pop()
            if not head.left:
                res.append(head.val)
                if head.right:
                    queue.append(head.right)
            else:
                left = head.left
                head.left = None
                queue.append(head)
                queue.append(left)

        return res

    def inorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        stack = []
        cur = root
        res = []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right

        return res