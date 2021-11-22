# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        l = len(preorder)
        if l == 0:
            return None

        dic = {}
        for i in range(l):
            dic[inorder[i]] = i

        def build(left, right):
            if left == right:
                return None

            root = TreeNode(preorder.pop(0))
            rootIndex = dic[root.val]

            root.left = build(left, rootIndex)
            root.right = build(rootIndex + 1, right)

            return root

        return build(0, l)

