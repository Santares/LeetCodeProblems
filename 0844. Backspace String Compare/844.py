class Solution:
    # space complexity is high
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s):
            res = ''
            for i in range(len(s)):
                if s[i] != '#':
                    res += s[i]
                else:
                    if len(res) > 0:
                        res = res[:len(res)-1]

            return res

        return helper(s) == helper(t)

    # Own solution based on online solution. Better space complexity
    def backspaceCompare2(self, s: str, t: str) -> bool:
        skips = 0
        skipt = 0
        i = len(s) - 1
        j = len(t) - 1
        while True:
            if i >= 0 and j >= 0:
                if s[i] == '#':
                    skips += 1
                    if t[j] == '#':
                        skipt += 1
                        i -= 1
                        j -= 1
                    else:
                        if skipt > 0:
                            i -= 1
                            j -= 1
                            skipt -= 1
                        else:
                            i -= 1
                else:
                    if skips > 0:
                        skips -= 1
                        i -= 1
                    else:
                        if t[j] == '#':
                            skipt += 1
                            j -= 1
                        else:
                            if skipt > 0:
                                j -= 1
                                skipt -= 1
                            else:
                                if s[i] != t[j]:
                                    return False
                                else:
                                    i -= 1
                                    j -= 1
            elif i >= 0 and j < 0:
                if s[i] == '#':
                    skips += 1
                else:
                    if skips > 0:
                        skips -= 1
                    else:
                        return False
                i -= 1
            elif i < 0 and j >= 0:
                if t[j] == '#':
                    skipt += 1
                else:
                    if skipt > 0:
                        skipt -= 1
                    else:
                        return False
                j -= 1
            else:
                break

        return True

    # Based on online solution
    def backspaceCompare3(self, s: str, t: str) -> bool:
        skips = 0
        skipt = 0
        i = len(s) - 1
        j = len(t) - 1
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    skips += 1
                    i -= 1
                elif skips == 0:
                    break
                else:
                    skips -= 1
                    i -= 1
            while j >= 0:
                if t[j] == '#':
                    skipt += 1
                    j -= 1
                elif skipt == 0:
                    break
                else:
                    skipt -= 1
                    j -= 1

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1

        return True