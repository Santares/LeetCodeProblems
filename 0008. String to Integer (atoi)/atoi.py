import re


class Solution:
    def myAtoi(self, s: str) -> int:
        minNum = (-1) * (1 << 31)
        maxNum = (1 << 31) - 1
        result = re.findall(r"^([+-]?\d+)", s.strip())
        if len(result) == 0:
            return 0

        num = result[0]
        if num[0] == '-':
            res = (-1) * int(num[1:])
        else:
            res = int(num)

        if res > maxNum:
            return maxNum
        elif res < minNum:
            return minNum
        else:
            return res


if __name__ == '__main__':
    solution = Solution()
    test = "dqfqf982"
    print(solution.myAtoi(test))
