from typing import List

class Solution:
    def findJudge1(self, n: int, trust: List[List[int]]) -> int:
        people = [-1] + [0] * n
        for a, b in trust:
            people[b] += 1
            people[a] -= 1

        for i in range(1, n + 1):
            if people[i] == n - 1:
                return i

        return -1

    def findJudge2(self, n: int, trust: List[List[int]]) -> int:

        people = [-1] + [0] * (n)

        for (source, target) in trust:
            # trusts someone, cant be
            people[source] = -1

            if people[target] != -1:
                people[target] += 1

        judges = [p for p, score in enumerate(people) if score == n - 1]

        if len(judges) == 1:
            return judges.pop()
        else:
            return -1



