# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []

        if not root:
            return res

        queue = [root]

        while queue:
            next_queue = []
            current = []
            for node in queue:
                current.append(node.val)
                if node.children:
                    for x in node.children:
                        next_queue.append(x)
            queue = next_queue
            res.append(current)

        return res
