import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cDict = collections.defaultdict(int)

        for c in magazine:
            cDict[c] += 1

        for c in ransomNote:
            cDict[c] -= 1
            if cDict[c] < 0:
                return False

        return True
