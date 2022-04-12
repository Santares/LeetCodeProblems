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

if __name__ == '__main__':
    solution = Solution()
    test = "()"
    test = "(())"
    test = "()()"
    test = "(()())"
    # test = "(((())))"
    # print(solution.scoreOfParentheses(test))
    print(solution.scoreOfParentheses2(test))