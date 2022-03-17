from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        i = 0
        for c in s:
            if dic[c] == 1:
                return i
            i += 1
        return -1

