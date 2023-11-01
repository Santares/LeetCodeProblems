from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        rods = defaultdict(int)
        count = 0

        i = 0
        while i < len(rings):
            color = rings[i]
            index = int(rings[i + 1])
            if rods[index] != 7:
                if color == "R":
                    rods[index] |= 1
                elif color == "G":
                    rods[index] |= 2
                else:
                    rods[index] |= 4
                if rods[index] == 7:
                    count += 1

            i += 2

        return count
