from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        buf = []
        pairs = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in pairs:
                buf.append(c)
            else:
                if len(buf) == 0:
                    return False
                lastC = buf[-1]
                if c == pairs[lastC]:
                    buf.pop()
                else:
                    return False

        if len(buf) == 0:
            return True
        else:
            return False

    def isValid2(self, s: str) -> bool:
        char_mapping = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in char_mapping:
                if not stack or char_mapping[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return not stack

    # 2023/08/17
    def isValid3(self, s: str) -> bool:
        queue = deque()
        dic = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in dic:
                queue.append(c)
            else:
                if not queue or dic[queue.pop()] != c:
                    return False
        return not queue


if __name__ == '__main__':
    test = "()"
    solution = Solution()
    print(solution.isValid2(test))
