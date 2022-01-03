from functools import lru_cache

class Solution:
    # acceptable, but maximum recursion depth exceeded in pycharm
    def knightDialer1(self, n: int) -> int:
        if n == 1:
            return 10

        dic = {}
        dic[0] = [4, 6]
        dic[1] = [6, 8]
        dic[2] = [7, 9]
        dic[3] = [4, 8]
        dic[4] = [0, 9, 3]
        dic[5] = []
        dic[6] = [7, 0, 1]
        dic[7] = [2, 6]
        dic[8] = [1, 3]
        dic[9] = [4, 2]

        @lru_cache(maxsize=None)
        def helper(current, m):
            if m == 0:
                return 1
            res = 0
            for x in dic[current]:
                res += helper(x, m - 1)
            return res

        res = 0
        for i in range(10):
            res += helper(i, n - 1)
        return res % (10 ** 9 + 7)

    # acceptable, but maximum recursion depth exceeded in pycharm
    def knightDialer2(self, n: int) -> int:
        if n == 1:
            return 10

        dic = {}
        dic[0] = [4, 6]
        dic[1] = [6, 8]
        dic[2] = [7, 9]
        dic[3] = [4, 8]
        dic[4] = [0, 9, 3]
        dic[5] = []
        dic[6] = [7, 0, 1]
        dic[7] = [2, 6]
        dic[8] = [1, 3]
        dic[9] = [4, 2]

        dp = {}
        for i in range(10):
            dp[i] = [-1] * n

        def helper(current, m):
            if m == 0:
                return 1
            if dp[current][m] != -1:
                return dp[current][m]
            res = 0
            for x in dic[current]:
                res += helper(x, m - 1)
            dp[current][m] = res
            return res

        res = 0
        for i in range(10):
            res += helper(i, n - 1)
        return res % (10 ** 9 + 7)

    # too slow
    def knightDialer3(self, n: int) -> int:
        if n == 1:
            return 10

        dic = {}
        # dic[0] = [4, 6]
        # dic[1] = [6, 8]
        # dic[2] = [7, 9]
        # dic[3] = [4, 8]
        # dic[4] = [0, 9, 3]
        # dic[5] = []
        # dic[6] = [7, 0, 1]
        # dic[7] = [2, 6]
        # dic[8] = [1, 3]
        # dic[9] = [4, 2]
        dic[0] = [4, 6]
        dic[1] = [6, 8]
        dic[2] = [7, 9]
        dic[3] = [4, 8]
        dic[4] = [0, 9, 3]
        dic[5] = []
        dic[6] = [7, 0, 1]
        dic[7] = [2, 6]
        dic[8] = [1, 3]
        dic[9] = [4, 2]

        dp = {}
        for i in range(10):
            dp[i] = [1] + [0] * (n - 1)

        for i in range(10):
            temp = dic[i]
            m = 1
            while temp and m < n:
                new_temp = []
                for j in temp:
                    dp[j][m] += 1
                    new_temp += dic[j]
                temp = new_temp
                m += 1

        res = 0
        for i in range(10):
            res += dp[i][-1]
        return res % (10 ** 9 + 7)

    # faster
    def knightDialer4(self, n: int) -> int:
        if n == 1:
            return 10

        dic = {}
        dic[0] = [4, 6]
        dic[1] = [6, 8]
        dic[2] = [7, 9]
        dic[3] = [4, 8]
        dic[4] = [0, 9, 3]
        dic[5] = []
        dic[6] = [7, 0, 1]
        dic[7] = [2, 6]
        dic[8] = [1, 3]
        dic[9] = [4, 2]

        dp = {}
        for i in range(10):
            dp[i] = [1] + [0] * (n - 1)

        count = 1
        while count < n:
            for i in range(10):
                for j in dic[i]:
                    dp[i][count] += dp[j][count - 1]
            count += 1

        res = 0
        for i in range(10):
            res += dp[i][-1]
        return res % (10 ** 9 + 7)

    # a little faster, less memory
    def knightDialer5(self, n: int) -> int:
        mod = 10 ** 9 + 7
        if n == 1:
            return 10

        dic = [[4 ,6] ,[6 ,8] ,[7 ,9] ,[4 ,8] ,[3 ,9 ,0] ,[] ,[1 ,7 ,0] ,[2 ,6] ,[1 ,3] ,[2 ,4]]  # helpful
        # dic[0] = [4, 6]
        # dic[1] = [6, 8]
        # dic[2] = [7, 9]
        # dic[3] = [4, 8]
        # dic[4] = [0, 9, 3]
        # dic[5] = []
        # dic[6] = [7, 0, 1]
        # dic[7] = [2, 6]
        # dic[8] = [1, 3]
        # dic[9] = [4, 2]

        last_dp = [1] * 10
        new_dp = [0] * 10

        count = 1
        while count < n:
            for i in range(10):
                for j in dic[i]:
                    new_dp[i] += last_dp[j]
                new_dp[i] %= mod  # speed up!
            count += 1
            last_dp = new_dp
            new_dp = [0] * 10


        res = sum(last_dp)
        return res % mod

    # online solution, fast!
    dp = [[1] * 10]

    def knightDialer6(self, n: int) -> int:
        mod = 10 ** 9 + 7
        table = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        for _ in range(len(self.dp), n):
            arr = []
            for i in range(10):
                arr.append(sum(self.dp[-1][n] for n in table[i]) % mod)
            self.dp.append(arr)

        return sum(self.dp[n - 1]) % mod


if __name__ == '__main__':
    solution = Solution()
    test = 1
    test = 2
    test = 3
    test = 10
    # test = 100
    # test = 1000
    # test = 3131
    print(solution.knightDialer5(test))
