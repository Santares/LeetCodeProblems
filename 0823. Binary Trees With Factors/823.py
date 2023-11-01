from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        arr.sort()
        map = {}
        for x in arr:
            map[x] = 1

        res = 0
        for i in range(len(arr)):
            x = arr[i]
            for j in range(i):
                y = arr[j]
                if x % y == 0 and x // y in map:
                    map[x] += map[x // y] * map[y]
            res += map[x]

        return res % mod

if __name__ == '__main__':
    s = Solution()
    test1 = [2,4,5,10]
    print(s.numFactoredBinaryTrees(test1))