from collections import Counter


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        for c in t:
            if c not in dic:
                return False
            else:
                dic[c] -= 1

        for c in dic:
            if dic[c] != 0:
                return False
        return True

    # very fast
    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
