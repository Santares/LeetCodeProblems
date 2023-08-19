from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = {1: set(["()"])}

        def helper(left, right, current):
            if right == 0:
                return current
            if left == right:
                res = set()
                for cur in current:
                    for old in dp[right]:
                        res.add(cur + old)
                return res
            else:
                res = set()
                if left > 0:
                    newCur = set([cur + "(" for cur in current])
                    res.update(helper(left - 1, right, newCur))

                newCur = set([cur + ")" for cur in current])
                res.update(helper(left, right - 1, newCur))
                return res

        for i in range(2, n + 1):
            dp[i] = helper(i - 1, i, ['('])

        return dp[n]

    # Based on online solution
    def generateParenthesis2(self, n: int) -> List[str]:
        res = []

        def helper(left, right, cur):
            if right == 0:
                res.append(cur)
                return
            if left > 0:
                helper(left - 1, right, cur + "(")
            if left < right:
                helper(left, right - 1, cur + ")")

        helper(n, n, "")

        return res

    # Based on online solution
    def generateParenthesis3(self, n: int) -> List[str]:
        dp = {0: set([""]), 1: set(["()"])}

        def helper(x):
            if x in dp:
                return dp[x]

            res = set()
            for i in range(0, x):
                for left in helper(i):
                    for right in helper(x - i - 1):
                        res.add(
                            "(" + left + ")" + right
                        )

            dp[x] = res
            return res

        return helper(n)

    # Based on online solution
    def generateParenthesis4(self, n: int) -> List[str]:
        dp = {0: set([""]), 1: set(["()"])}

        def helper(x):
            res = set()
            for old in dp[x - 1]:
                for j in range(2 * x):
                    res.add(old[0:j] + "()" + old[j:])

            dp[x] = res
            return

        for i in range(2, n + 1):
            helper(i)

        return dp[n]
