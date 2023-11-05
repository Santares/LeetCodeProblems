from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            newS = ''.join(sorted(list(s)))
            groups[newS].append(s)

        return list(groups.values())
