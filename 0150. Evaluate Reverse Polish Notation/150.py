from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for t in tokens:
            if t == '+':
                y = stack.pop()
                x = stack.pop()
                stack.append(x+y)
            elif t == '-':
                y = stack.pop()
                x = stack.pop()
                stack.append(x-y)
            elif t == '*':
                y = stack.pop()
                x = stack.pop()
                stack.append(x*y)
            elif t == '/':
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x/y))
            else:
                stack.append(int(t))

        return stack.pop()


if __name__ == '__main__':
    s = Solution()
    test = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(s.evalRPN(test))
