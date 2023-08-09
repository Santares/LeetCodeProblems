class Solution:
    # A little slow
    def minWindow(self, s: str, t: str) -> str:
        last = ''
        left = 0
        dic = {}
        for c in t:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1

        def check():
            for key, val in dic.items():
                if val > 0:
                    return False
            return True

        for right in range(len(s)):
            if s[right] in dic:
                dic[s[right]] -= 1
                while True:
                    if s[left] in dic:
                        if dic[s[left]] < 0:
                            dic[s[left]] += 1
                            left += 1
                        else:
                            break
                    else:
                        left += 1
                if check() and (last == '' or len(last) > (right - left + 1)):
                    last = s[left:right + 1]

        return last

    # Improved version of 1. Much faster
    def minWindow2(self, s: str, t: str) -> str:
        last = ''
        left = 0
        dic = {}
        valid = 0
        for c in t:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
                valid += 1

        for right in range(len(s)):
            if s[right] in dic:
                dic[s[right]] -= 1
                if dic[s[right]] == 0:
                    valid -= 1
                while True:
                    if s[left] in dic:
                        if dic[s[left]] < 0:
                            dic[s[left]] += 1
                            left += 1
                        else:
                            break
                    else:
                        left += 1
                if valid == 0 and (last == '' or len(last) > (right - left + 1)):
                    last = s[left:right + 1]

        return last
