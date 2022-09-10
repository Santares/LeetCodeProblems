from math import ceil
from typing import List
from collections import Counter


class Solution:
    # slow
    def minSetSize(self, arr: List[int]) -> int:
        length = len(arr)
        dic = {}
        for x in arr:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1

        dic = sorted(dic.items(), key=lambda y: y[1], reverse=True)

        newLen = length
        res = 0
        count = 0
        while newLen >= (length // 2) + 1:
            newLen -= dic[count][1]
            res += 1
            count += 1

        return res

    # improved version of 1, slow too
    def minSetSize2(self, arr: List[int]) -> int:
        length = len(arr)
        dic = Counter(arr).most_common()
        newLen = length
        res = 0
        for key, count in dic:
            newLen -= count
            res += 1
            if newLen <= (length + 1) // 2:
                return res

        return res

    # online solution
    def minSetSize3(self, arr: List[int]) -> int:
        res, n, A = 0, ceil(len(arr) / 2), sorted(Counter(A).values(), reverse=True)
        while n > 0:
            n -= A[res]
            res += 1
        return res



if __name__ == '__main__':
    s = Solution()
    test = [3,3,3,3,5,5,5,2,2,7]
    test = [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]

    print(s.minSetSize2(test))