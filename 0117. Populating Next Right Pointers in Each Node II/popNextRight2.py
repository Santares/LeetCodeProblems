from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        queue = [root]

        while queue:
            temp = []
            for i in range(len(queue) - 1):
                node = queue[i]
                node.next = queue[i + 1]
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            node = queue[-1]
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)

            queue = temp

        return root

    # online solution, faster, in-place
    def connect2(self, root: 'Node') -> 'Node':
        dummy = Node(-1)
        current = dummy
        head = root

        while head:
            while head:
                if head.left:
                    current.next = head.left
                    current = current.next
                if head.right:
                    current.next = head.right
                    current = current.next

                head = head.next

            head = dummy.next
            dummy.next = None
            current = dummy

        return root