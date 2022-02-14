import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(re.findall("[a-z0-9]+", s.strip().lower()))

        s = "".join(s.strip().lower().split())
        for i in range(len(s)):
            if s[i] != s[i * -1 - 1]:
                return False

        return True

    # faster
    def isPalindrome2(self, s: str) -> bool:
        s = "".join(re.findall("[a-z0-9]+", s.strip().lower()))
        return s == s[::-1]

    def isPalindrome3(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s.lower()))
        return s == s[::-1]

if __name__ == '__main__':
    test = "A man, a plan, a canal: Panama"
    test = "0P"
    s = Solution()
    print(s.isPalindrome(test))