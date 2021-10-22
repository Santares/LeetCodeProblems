class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        l = s.split()
        l.reverse()
        return ' '.join(l)

    # online solution
    def reverseWords2(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


if __name__ == '__main__':
    solution = Solution()
    test = ""
    print(solution.reverseWords(test))
