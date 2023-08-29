from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def insert(root, node):
            if node is None:
                return
            if root.val > node.val:
                if root.left:
                    insert(root.left, node)
                else:
                    root.left = node
            else:
                if root.right:
                    insert(root.right, node)
                else:
                    root.right = node

        head = root
        last = None
        while head:
            if head.val > key:
                last = head
                head = head.left
            elif head.val < key:
                last = head
                head = head.right
            else:
                if last is None:
                    if head.left:
                        root = head.left
                        insert(head.left, head.right)
                    elif head.right:
                        root = head.right
                        root.left = head.left
                    else:
                        return None
                elif head.left:
                    if last.val > head.val:
                        last.left = head.left
                    else:
                        last.right = head.left
                    insert(head.left, head.right)
                elif head.right:
                    if last.val > head.val:
                        last.left = head.right
                    else:
                        last.right = head.right
                else:
                    if last.val > head.val:
                        last.left = None
                    else:
                        last.right = None
                break

        return root

    # based on online solution, better BST delete, not faster
    def deleteNode2(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left and root.right:
                minNode = self.getMin(root.right)
                root.val, minNode.val = minNode.val, root.val
                root.right = self.deleteNode(root.right, minNode.val)
            elif root.left or root.right:
                return root.left if root.left else root.right
            else:
                return None

        return root

    def getMin(self, root):
        while root.left:
            root = root.left
        return root

    def deleteNode3(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        superRoot = TreeNode(0)
        superRoot.left = root
        parent = superRoot

        def helper(root, key, parent, isLeft):
            if root is None:
                return

            if root.val == key:
                if not root.left and not root.right:
                    if isLeft:
                        parent.left = None
                    else:
                        parent.right = None
                elif root.left:
                    if isLeft:
                        parent.left = root.left
                    else:
                        parent.right = root.left
                    rotate(root.left, root.right)
                else:
                    if isLeft:
                        parent.left = root.right
                    else:
                        parent.right = root.right
                    rotate(root.right, root.left)

            elif root.val > key:
                helper(root.left, key, root, True)
            else:
                helper(root.right, key, root, False)

            return root

        def rotate(root, subTree):
            if not subTree:
                return
            if root.val < subTree.val:
                if root.right:
                    rotate(root.right, subTree)
                else:
                    root.right = subTree
            else:
                if root.left:
                    rotate(root.left, subTree)
                else:
                    root.left = subTree

        helper(root, key, parent, True)
        return superRoot.left

    # Based on online solution, improved version of solution 3
    def deleteNode4(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def insert(root, subTree):
            if not subTree:
                return
            while root.right:
                root = root.right
            root.right = subTree

        if root is None:
            return

        if root.val == key:
            if not root.left and not root.right:
                return None
            elif root.left:
                insert(root.left, root.right)
                return root.left
            else:
                return root.right

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root


if __name__ == '__main__':
    s = Solution()
    test = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    key = 3
    print(s.deleteNode3(test, key))