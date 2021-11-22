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