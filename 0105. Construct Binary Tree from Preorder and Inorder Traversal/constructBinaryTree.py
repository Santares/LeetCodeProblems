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

    # 20231103
    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexMap = {}
        for i, x in enumerate(inorder):
            indexMap[x] = i

        self.index = 0

        def helper(left, right):
            if left > right:
                return None

            val = preorder[self.index]
            root = TreeNode(val)
            self.index += 1

            if left != right:
                mid = indexMap[val]
                root.left = helper(left, mid - 1)
                root.right = helper(mid + 1, right)

            return root

        return helper(0, len(preorder) - 1)

