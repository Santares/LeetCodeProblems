from collections import Counter, defaultdict
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        houses = []

        res = 0
        lastM = 0
        lastP = 0
        lastG = 0

        cumTravel = [0]

        for i, g in enumerate(garbage):
            h = Counter(g)
            houses.append(h)
            if i > 0:
                cumTravel.append(cumTravel[-1] + travel[i - 1])
            if houses[-1]['M'] != 0:
                lastM = i
            if houses[-1]['P'] != 0:
                lastP = i
            if houses[-1]['G'] != 0:
                lastG = i
            res += h['M']
            res += h['P']
            res += h['G']

        res += cumTravel[lastM]
        res += cumTravel[lastP]
        res += cumTravel[lastG]

        return res

    # Improved version
    def garbageCollection2(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        last = defaultdict(int)

        cumTravel = [0]

        for i, g in enumerate(garbage):
            res += len(g)
            if i > 0:
                cumTravel.append(cumTravel[-1] + travel[i - 1])
            for c in g:
                last[c] = i

        res += cumTravel[last['M']]
        res += cumTravel[last['P']]
        res += cumTravel[last['G']]

        return res
