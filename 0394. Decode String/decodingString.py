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


if __name__ == '__main__':
    soultion = Solution()
    test = "3[a]2[bc]"
    # test = "100[leetcode]"
    print(soultion.decodeString(test))
