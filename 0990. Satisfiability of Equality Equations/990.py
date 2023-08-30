from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                parent[y] = x

        parent = {}

        for eq in equations:
            x = eq[0]
            y = eq[-1]
            if x not in parent:
                parent[x] = x
            if y not in parent:
                parent[y] = y

            if eq[1] == "=":
                union(x, y)

        for eq in equations:
            x = eq[0]
            y = eq[-1]
            if eq[1] == "!":
                if find(x) == find(y):
                    return False

        return True