from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

    def reverseString2(self, s: List[str]) -> None:
        l = len(s)
        mid = l // 2
        i = 0
        while i < mid:
            temp = s[i]
            s[i] = s[l - i - 1]
            s[l - i - 1] = temp
            i += 1

    # not as required
    def reverseStringE(self, s: str) -> str:
        if len(s) <= 1:
            return s
        mid = len(s) // 2
        left = s[:mid]
        right = s[mid:]
        return self.reverseStringE(right) + self.reverseStringE(left)


if __name__ == '__main__':
    solution = Solution()

    test1 = ["h", "e", "l", "l", "o"]
    test2 = ["H", "a", "n", "n", "a", "h"]
    test3 = ["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ", "a", " ", "c", "a", "n", "a", "l", ":",
     " ", "P", "a", "n", "a", "m", "a"]
    # print(solution.reverseString2(test1))


    print(solution.reverseStringE("12345"))
