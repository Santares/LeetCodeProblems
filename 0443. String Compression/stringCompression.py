from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return 0
        i = 0
        j = 0
        count = 0
        curr = chars[0]

        while j < len(chars):
            if chars[j] == curr:
                count += 1
                j += 1
            else:
                chars[i] = curr
                i += 1
                z = []
                if count > 1:
                    while count >= 1:
                        z.append(str(count % 10))
                        count = count // 10
                if len(z) > 0:
                    chars[i:i + len(z)] = z[::-1]
                    i += len(z)
                curr = chars[j]
                count = 1
                j += 1

        chars[i] = curr
        i += 1
        z = []
        if count > 1:
            while count >= 1:
                z.append(str(count % 10))
                count = count // 10
        if len(z) > 0:
            chars[i:i + len(z)] = z[::-1]
            i += len(z)

        return i

    def compress2(self, chars: List[str]) -> int:
        c = 1
        for i in range(len(chars) - 1, -1, -1):
            if i > 0 and chars[i - 1] == chars[i]:
                c += 1
                chars.pop(i)
            else:
                if c > 1:
                    for j in str(c)[::-1]:
                        chars.insert(i + 1, j)
                    c = 1
        return len(chars)
