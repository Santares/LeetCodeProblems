from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = [Counter(word) for word in words]

        final = counts[0]
        for c in final:
            for count in counts[1:]:
                final[c] = min(final[c], count[c])

        res = []
        for c in final:
            res += [c] * final[c]

        return res

    def commonChars2(self, words: List[str]) -> List[str]:
        final = Counter(words[0])

        for word in words[1:]:
            count = Counter(word)
            final &= count

        res = []
        for c in final:
            res += [c] * final[c]

        return res
