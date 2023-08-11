from typing import List


class Solution:
    # too slow
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        def helper(rest_amount, rest_coins):
            if rest_amount == 0:
                return 0
            if len(rest_coins) == 0:
                return -1
            if rest_amount < rest_coins[0]:
                return helper(rest_amount, rest_coins[1:])
            c = rest_coins[0]
            x = rest_amount // c
            res = -1
            for i in range(x, -1, -1):
                tmp = helper(rest_amount - c * i, rest_coins[1:])
                if tmp != -1:
                    if res == -1:
                        res = tmp + i
                    else:
                        res = min(res, tmp + i)
            return res

        return helper(amount, coins)

    # online solution
    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for c in coins:
                if x >= c:
                    dp[x] = min(dp[x], 1 + dp[x - c])
        if dp[-1] == amount + 1:
            return -1
        else:
            return dp[-1]

    # 20230810:
    def coinChange3(self, coins: List[int], amount: int) -> int:
        mem = {0: 0}
        coins.sort(reverse=True)

        def helper(x):
            if x in mem:
                return mem[x]

            res = -1
            for i in coins:
                if i <= x:
                    newRes = helper(x - i)
                    if newRes == -1:
                        continue
                    elif res == -1:
                        res = newRes + 1
                    else:
                        res = min(newRes + 1, res)

            mem[x] = res
            return res

        return helper(amount)

    # Improved version of solution3, less space
    def coinChange4(self, coins: List[int], amount: int) -> int:
        mem = [-1] * (amount + 1)
        mem[0] = 0

        for i in range(1, amount + 1):
            for x in coins:
                if x <= i:
                    if mem[i - x] != -1:
                        if mem[i] == -1:
                            mem[i] = mem[i - x] + 1
                        else:
                            mem[i] = min(mem[i], mem[i - x] + 1)

        return mem[amount]

if __name__ == '__main__':
    solution = Solution()
    # test1 =[3,7,405,436]
    # test2 = 8839
    test1 = [1,2,5]
    test2 = 11
    print(solution.coinChange(test1, test2))