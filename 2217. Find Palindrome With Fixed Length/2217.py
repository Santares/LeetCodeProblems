from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        res = []
        n = 9 * (10 ** ((intLength-1)//2))
        for x in queries:
            if x > n:
                res.append(-1)
            else:
                if intLength == 1:
                    res.append(x)
                else:
                    m = 10 ** (intLength//2)
                    num = 10 ** (intLength - 1) + m * (x-1)
                    num = str(num)[:(intLength+1)//2] + str(num)[intLength//2-1::-1]
                    res.append(int(num))


        return res

    # Online solution
    def kthPalindrome2(self, queries: List[int], intLength: int) -> List[int]:
        l = (intLength + 1) // 2  # 可以唯一确定回文数的前半部分的长度
        start = 10 ** (l - 1) - 1  # start + k 即为第 k 个 l 位无前导零整数
        limit = 10 ** l - 1  # l 位无前导零整数的上界
        res = []

        # 将前半部分恢复为对应的回文数
        def recover(num: int) -> int:
            if intLength % 2 == 0:
                return int(str(num) + str(num)[::-1])
            else:
                return int(str(num)[:-1] + str(num)[::-1])

        # 依次处理询问
        for query in queries:
            if start + query > limit:
                # 不存在
                res.append(-1)
                continue
            res.append(recover(start + query))
        return res


if __name__ == '__main__':
    s = Solution()
    test1 = [1,2,3,4,5,78, 90]
    test2 = 3
    print(s.kthPalindrome(test1, test2))