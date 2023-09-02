from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        used = [False] * n
        self.res = []
        tickets.sort()

        def dfs(i, cur):
            if i >= n:
                self.res = cur
                return True

            for j in range(n):
                if not used[j] and (not cur or tickets[j][0] == cur[-1]):
                    cur.append(tickets[j][1])
                    used[j] = True
                    if dfs(i + 1, cur):
                        return True
                    used[j] = False
                    cur.pop()

            return False

        dfs(0, ["JFK"])

        return self.res
