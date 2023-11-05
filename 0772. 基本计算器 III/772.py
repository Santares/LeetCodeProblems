class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(stack):
            res = stack.pop(0)
            while stack:
                op = stack.pop(0)
                y = stack.pop(0)
                if op == '+':
                    res += y
                else:
                    res -= y
            return res

        def helper(index):
            stack = []
            flag = False
            cur = ''
            while index < len(s):
                c = s[index]
                if c in '0123456789':
                    cur += c
                    index += 1
                elif c in '+-':
                    if cur != '':
                        x = int(cur)
                        if flag:
                            op = stack.pop()
                            y = stack.pop()
                            if op == '*':
                                stack.append(y * x)
                            else:
                                stack.append(y // x)
                            flag = False
                        else:
                            stack.append(x)
                    stack.append(c)
                    index += 1
                    cur = ''
                elif c in '*/':
                    if cur != '':
                        x = int(cur)
                        if flag:
                            op = stack.pop()
                            y = stack.pop()
                            if op == '*':
                                stack.append(y * x)
                            else:
                                stack.append(int(y / x))
                        else:
                            stack.append(x)
                    flag = True
                    stack.append(c)
                    index += 1
                    cur = ''
                elif c == '(':
                    x, index = helper(index + 1)
                    if flag:
                        op = stack.pop()
                        y = stack.pop()
                        if op == '*':
                            stack.append(y * x)
                        else:
                            stack.append(int(y / x))
                        flag = False
                    else:
                        stack.append(x)
                elif c == ')':
                    if cur != '':
                        x = int(cur)
                        if flag:
                            op = stack.pop()
                            y = stack.pop()
                            if op == '*':
                                stack.append(y * x)
                            else:
                                stack.append(y // x)
                        else:
                            stack.append(x)
                    return evaluate(stack), index + 1

            if cur != '':
                x = int(cur)
                if flag:
                    op = stack.pop()
                    y = stack.pop()
                    if op == '*':
                        stack.append(y * x)
                    else:
                        stack.append(int(y / x))
                else:
                    stack.append(x)
            return evaluate(stack), index + 1

        x, _ = helper(0)
        return x

    def calculate2(self, s: str) -> int:
        def addNum(x, stack, lastSign):
            if lastSign == '*':
                stack.append(stack.pop() * x)
            elif lastSign == '/':
                stack.append(int(stack.pop() / x))
            elif lastSign == '-':
                stack.append(-x)
            else:
                stack.append(x)

        def helper(index):
            stack = []
            lastSign = ''
            cur = ''
            while index < len(s):
                c = s[index]
                if c in '0123456789':
                    cur += c
                    index += 1
                elif c in '+-':
                    if cur != '':
                        x = int(cur)
                        addNum(x, stack, lastSign)
                    lastSign = c
                    index += 1
                    cur = ''
                elif c in '*/':
                    if cur != '':
                        x = int(cur)
                        addNum(x, stack, lastSign)
                    lastSign = c
                    index += 1
                    cur = ''
                elif c == '(':
                    x, index = helper(index + 1)
                    addNum(x, stack, lastSign)
                    lastSign = ''
                elif c == ')':
                    if cur != '':
                        x = int(cur)
                        addNum(x, stack, lastSign)
                    return sum(stack), index + 1

            if cur != '':
                x = int(cur)
                addNum(x, stack, lastSign)
            return sum(stack), index + 1

        x, _ = helper(0)
        return x


if __name__ == '__main__':
    s = Solution()
    test = "1+1"
    test = "6-4/2"
    test = "2*(5+5*2)/3+(6/2+8)"
    print(s.calculate(test))
