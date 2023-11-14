from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        chars = defaultdict(list)
        counts = {}
        for i, c in enumerate(s):
            chars[c].append(i)

        for c in chars:
            counts[c] = []

        for c in s:
            for k in counts:
                if k == c:
                    count = 1
                else:
                    count = 0
                if counts[k]:
                    counts[k].append(counts[k][-1] + count)
                else:
                    counts[k].append(count)

        res = 0
        for c in chars:
            pos = chars[c]
            if len(pos) < 2:
                continue
            else:
                i = pos[0]
                j = pos[-1]
                for c in chars:
                    if counts[c][j - 1] - counts[c][i] > 0:
                        res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    test = "aabca"
    print(s.countPalindromicSubsequence(test))