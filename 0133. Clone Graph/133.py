# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    # Based on online solution. BFS
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque([node])
        newNode = Node(node.val)
        visited = {node}
        dic = {node:newNode}

        while queue:
            n = queue.popleft()
            newNode = dic[n]
            for nxt in n.neighbors:
                if nxt not in dic:
                    newNxt = Node(nxt.val)
                    dic[nxt] = newNxt
                newNode.neighbors.append(dic[nxt])

                if nxt not in visited:
                    queue.append(nxt)
                    visited.add(nxt)

        return dic[node]

    # DFS
    def cloneGraph2(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        newNode = Node(node.val)
        visited = set()
        dic = {node: newNode}

        def helper(cur):
            if cur in visited:
                return

            visited.add(cur)

            newCur = dic[cur]
            for nxt in cur.neighbors:
                if nxt not in dic:
                    newNxt = Node(nxt.val)
                    dic[nxt] = newNxt
                newCur.neighbors.append(dic[nxt])
                helper(nxt)

        helper(node)
        return newNode

if __name__ == '__main__':
    s = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node3.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node4.neighbors = [node1, node3]

    print(s.cloneGraph(node1))