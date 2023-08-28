from collections import defaultdict
from typing import List


class Solution:
    # dp
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        dp = defaultdict(int)
        pairs.sort(key=lambda x: x[0])

        for start, end in pairs:
            res = 1
            for key in dp:
                if key < start:
                    res = max(res, dp[key] + 1)
            dp[end] = max(dp[end], res)


        res = 0
        for key, val in dp.items():
            res = max(res, val)
        return res

    # Based on online solution. Greedy
    def findLongestChain2(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        last = float("-inf")
        length = 0
        for start, end in pairs:
            if start > last:
                length += 1
                last = end

        return length

    # Based on online solution. DP + greedy
    def findLongestChain3(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])
        dp = [1] * len(pairs)

        for i in range(len(pairs)):
            for j in range(i - 1, -1, -1):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = dp[j] + 1
                    break

        return max(dp)

