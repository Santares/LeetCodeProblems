# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pPath = []
        self.qPath = []

        def helper(root, path):
            path.append(root)

            if root.val == p.val:
                self.pPath = list(path)
            if root.val == q.val:
                self.qPath = list(path)

            if self.pPath and self.qPath:
                return

            if root.left:
                helper(root.left, path)
                path.pop()
            if root.right:
                helper(root.right, path)
                path.pop()

            return

        helper(root, [])

        res = None
        for i in range(min(len(self.pPath), len(self.qPath))):
            if self.pPath[i] != self.qPath[i]:
                return res
            else:
                res = self.pPath[i]

        return res

    # Online solution
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left is None:
            return right
        else:
            return left