class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        l = len(s)

        def helper(string, index):
            res = 0
            while index < l:
                if string[index] == "(":
                    if string[index + 1] == ")":
                        res += 1
                        index += 2
                    else:
                        score, newIndex = helper(string, index + 1)
                        res += 2 * score
                        index = newIndex
                else:
                    return res, index + 1
            return res, index + 1

        res, i = helper(s, 0)
        return res

    # online solution, O(N) cleaver
    def scoreOfParentheses2(self, S):
        stack, cur = [], 0
        for i in S:
            if i == '(':
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)
        return cur

    # Another version of solution 2
    def scoreOfParentheses2_2(self, s: str) -> int:
        stk = [0]
        for c in s:
            if c == '(':
                stk.append(0)
            else:
                cur = stk.pop()
                stk.append(stk.pop() + max(cur * 2, 1))
        return stk[-1]

    # 2023/09/05
    def scoreOfParentheses3(self, s: str) -> int:
        res = 0
        stack = []
        level = 0
        for c in s:
            if c == '(':
                level += 1
            else:
                if stack and stack[-1][1] > level:
                    cur = 0
                    while stack and stack[-1][1] > level:
                        cur += stack.pop()[0]
                    cur *= 2
                else:
                    cur = 1
                stack.append([cur, level])
                level -= 1

        return sum(x[0] for x in stack)

    # Based on online solution
    def scoreOfParentheses4(self, s: str) -> int:
        res = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                cur = stack.pop()
                if cur:
                    cur *= 2
                else:
                    cur = 1
                if stack:
                    stack[-1] += cur
                else:
                    stack.append(cur)

        return stack[-1]


if __name__ == '__main__':
    solution = Solution()
    test = "()"
    test = "(())"
    test = "()()"
    # test = "(()())"
    # test = "(((())))"
    # print(solution.scoreOfParentheses(test))
    print(solution.scoreOfParentheses3(test))
