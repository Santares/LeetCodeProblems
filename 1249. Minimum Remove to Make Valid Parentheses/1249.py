class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp = ""
        res = ""
        stack = 0

        for c in s:
            if c == "(":
                stack += 1
                temp += c
            elif c == ")":
                if stack > 0:
                    stack -= 1
                    temp += c
                else:
                    pass
            else:
                temp += c

        stack = 0
        for c in temp[::-1]:
            if c == ")":
                stack += 1
                res += c
            elif c == "(":
                if stack > 0:
                    stack -= 1
                    res += c
                else:
                    pass
            else:
                res += c

        return res[::-1]

