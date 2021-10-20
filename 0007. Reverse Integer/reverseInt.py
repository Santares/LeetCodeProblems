class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if x < 0:
            s = s[:0:-1]
            y = -1
        else:
            s = s[::-1]
            y = 1

        y = y * int(s)

        if y > 2 ** 31 - 1 or y < -1 * 2 ** 31:
            return 0

        return y


if __name__ == '__main__':
    solution = Solution()
    test = 1534236469
    print(solution.reverse(test))