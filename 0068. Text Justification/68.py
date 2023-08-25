from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        cur = []
        curCnt = 0
        i = 0
        while i < len(words):
            word = words[i]
            if maxWidth - curCnt >= len(word):
                cur.append(word)
                curCnt += len(word)
                if curCnt == maxWidth:
                    lines.append(cur)
                    cur = []
                    curCnt = 0
                else:
                    cur[-1] += ' '
                    curCnt += 1
                i += 1
            else:
                cur[-1] = cur[-1].strip()
                lines.append(cur)
                cur = []
                curCnt = 0
        if cur:
            lines.append(cur)

        for line in lines[:-1]:
            res = maxWidth - len(''.join(line))
            i = 0
            while res > 0:
                line[i] += ' '
                i = (i + 1) % len(line)
                if len(line) > 1 and i == len(line) - 1:
                    i = (i + 1) % len(line)
                res -= 1

        line = lines[-1]
        res = maxWidth - len(''.join(line))
        line[-1] += ' ' * res

        return [''.join(line) for line in lines]


if __name__ == '__main__':
    s = Solution()
    # test1 = ["This", "is", "an", "example", "of", "text", "justification."]
    test1 = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
    test2 = 16
    print(s.fullJustify(test1, test2))
