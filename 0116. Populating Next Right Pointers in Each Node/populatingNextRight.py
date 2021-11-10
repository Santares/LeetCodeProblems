

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
            return root

        queue = []
        queue.append(root)
        while queue:
            temp = []
            for i in range(len(queue) - 1):
                node = queue[i]
                queue[i].next = queue[i + 1]
                if node.left:
                    temp += [node.left, node.right]
            queue[-1].next = None
            if queue[-1].left:
                temp += [queue[-1].left, queue[-1].right]
            queue = temp

        return root