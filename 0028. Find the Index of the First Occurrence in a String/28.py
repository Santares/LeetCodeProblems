class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        for i in range(len(haystack)-l+1):
            if haystack[i:i+l] == needle:
                return i
        return -1

    # KMP algorithm
    def strStr2(self, haystack: str, needle: str) -> int:
        def helper(s):
            prefs = [0] * len(s)
            i = 0
            for j in range(1, len(s)):
                while i > 0 and s[i] != s[j]:
                    i = prefs[i - 1]
                if s[i] == s[j]:
                    i += 1
                prefs[j] = i
            return prefs

        prefs = helper(needle)
        index = 0
        for i in range(len(haystack)):
            while index > 0 and needle[index] != haystack[i]:
                index = prefs[index - 1]

            if needle[index] == haystack[i]:
                index += 1

            if index == len(needle):
                return i - index + 1

        return -1

    def helper(self, s):
        res = 0
        l = len(s)
        for i in range(l // 2 + 1):
            if s[:i + 1] == s[l - i - 1:]:
                res = i + 1

        return res

    def helper2(self, s):
        prefs = [0] * len(s)
        i = 0
        for j in range(1, len(s)):
            while i > 0 and s[i] != s[j]:
                i = prefs[i-1]
            if s[i] == s[j]:
                i += 1
            prefs[j] = i
        return prefs


if __name__ == '__main__':
    s = Solution()
    test1 = "mississippi"
    test2 = "issip"
    # # test1 = "ababcaababcaabc"
    # # test2 = "ababcaabc"
    # test1 = "a"
    # test2 = "a"
    # # test1 = "leetcode"
    # # test2 = "leeto"
    # # test1 = "sadbutsad"
    # # test2 = "sad"
    # test1 = "aabaaabaaac"
    # test2 = "aabaaac"
    print(s.strStr2(test1, test2))
    # print(s.helper2("ababcaab"))
    # print(s.helper2("issip"))
    # print(s.helper2("aabaaac"))
