from collections import Counter
from typing import List


class Solution:
    # slow
    def partitionLabels(self, s: str) -> List[int]:
        new = {}
        old = Counter(s)
        res = []
        count = 0
        for c in s:
            count += 1
            if c not in new:
                new[c] = 1
            else:
                new[c] += 1

            cut = True
            for k in new:
                if 0 < new[k] < old[k]:
                    cut = False
                    break
                elif new[k] == old[k]:
                    new[k] = -1
            if cut:
                res.append(count)
                count = 0

        return res

    # online reference, very fast
    def partitionLabels2(self, s: str) -> List[int]:
        res = []
        last = {}
        for i, c in enumerate(s):
            last[c] = i

        seen = set()
        flag = 0
        start = 0
        for i, c in enumerate(s):
            if c not in seen:
                flag = max(flag, last[c])
                seen.add(c)
            if i == flag:
                res.append(flag - start + 1)
                start = flag + 1

        return res

    # 2023/08/31
    def partitionLabels3(self, s: str) -> List[int]:
        dic = {}
        for i, x in enumerate(s):
            dic[x] = i

        res = []

        def helper(i):
            if i >= len(s):
                return 0
            end = dic[s[i]]
            j = i + 1
            while j < end:
                c = s[j]
                if dic[c] > end:
                    end = dic[c]
                j += 1

            return end - i + 1

        i = 0
        while i < len(s):
            r = helper(i)
            if r != 0:
                res.append(r)
                i += r

        return res