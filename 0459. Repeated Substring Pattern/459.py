class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        init = 0
        last = 0
        sec = last + 1
        while sec <= len(s) // 2:
            while sec < len(s) - 1 and s[sec] != s[init]:
                sec += 1
            pattern = s[init:sec]
            l = len(pattern)
            if len(s) % l != 0:
                sec += 1
                continue
            else:
                start = sec
                valid = True
                while start < len(s):
                    if s[start:start + l] != pattern:
                        valid = False
                        break
                    else:
                        start += l
                if valid:
                    return True
                else:
                    sec += 1

        return False


    def repeatedSubstringPattern2(self, s: str) -> bool:
        ds = s + s
        for i in range(1, len(s)):
            if ds[i: i + len(s)] == s:
                return True
        return False

    # Use built in function
    def repeatedSubstringPattern3(self, s: str) -> bool:
        ds = s + s
        return s in ds[1:-1]


if __name__ == '__main__':
    s = Solution()
    test = "abac"
    print(s.repeatedSubstringPattern(test))
