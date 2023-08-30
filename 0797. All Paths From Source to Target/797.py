from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        def helper(node, cur):
            cur.append(node)
            if node == n-1:
                res.append(cur)
            else:
                for newNode in graph[node]:
                    helper(newNode, list(cur))

        helper(0, [])

        return res

    def allPathsSourceTarget2(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)

        def helper(node, cur):
            if node == n - 1:
                res.append(list(cur))
            else:
                for newNode in graph[node]:
                    cur.append(newNode)
                    helper(newNode, cur)
                    cur.pop()

        helper(0, [0])

        return res
