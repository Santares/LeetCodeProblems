import re

class Solution:
    def decodeString(self, s: str) -> str:

        def helper(counts, s):
            n = len(s)
            i = 0
            res = ""
            while i < n:
                if s[i] >= 'a' and s[i] <= 'z':
                    res += s[i]
                    i += 1
                else:
                    temp = re.findall(r"(\d+).*", s[i:])[0]
                    i += len(temp)
                    newCounts = int(temp)
                    stack = 0
                    for j in range(i + 1, n):
                        if s[j] == '[':
                            stack += 1
                        elif s[j] == ']':
                            if stack:
                                stack -= 1
                            else:
                                res += helper(newCounts, s[i + 1:j])
                                i = j + 1
                                break

            return counts * res

        return helper(1, s)

    # not using re, a little faster, a little more space
    def decodeString2(self, s: str) -> str:

        def helper(counts, s):
            n = len(s)
            i = 0
            res = ""
            while i < n:
                if s[i] >= 'a' and s[i] <= 'z':
                    res += s[i]
                    i += 1
                else:
                    temp = ""
                    while True:
                        if s[i] == '[':
                            break
                        else:
                            temp += s[i]
                            i += 1

                    newCounts = int(temp)
                    stack = 0
                    for j in range(i + 1, n):
                        if s[j] == '[':
                            stack += 1
                        elif s[j] == ']':
                            if stack:
                                stack -= 1
                            else:
                                res += helper(newCounts, s[i + 1:j])
                                i = j + 1
                                break

            return counts * res

        return helper(1, s)

    # 2023/09/18
    def decodeString3(self, s: str) -> str:
        def helper(i):
            res = ""
            m = 0

            while i < len(s):
                c = s[i]
                if c in "0123456789":
                    if m != 0:
                        m = m * 10 + int(c)
                    else:
                        m = int(c)
                elif c == '[':
                    i, cur = helper(i + 1)
                    res += m * cur
                    m = 0
                elif c == ']':
                    return i, res

                else:
                    res += c

                i += 1

            # return i, res

        s += ']'
        _, res = helper(0)

        return res

    # 20231104
    def decodeString4(self, s: str) -> str:
        stack = []
        i = 0
        m = 0
        cur = ''
        while i < len(s):
            c = s[i]
            if c in '0123456789':
                if cur != '':
                    stack.append(cur)
                    cur = ''
                m = m * 10 + int(c)
            elif c == '[':
                stack.append(m)
                m = 0
            elif c == ']':
                cur = stack.pop() * cur
                if stack and type(stack[-1]) is not int:
                    cur = stack.pop() + cur
            else:
                cur += c
            i += 1

        if cur != '':
            stack.append(cur)

        return ''.join(stack)


if __name__ == '__main__':
    soultion = Solution()
    test = "3[a]2[bc]"
    test = "3[a2[c]]"
    # test = "100[leetcode]"
    print(soultion.decodeString4(test))
