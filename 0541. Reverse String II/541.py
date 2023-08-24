class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = 0
        res = ""
        while l < len(s):
            s1 = s[l:l + k]
            s2 = s[l + k:l + 2 * k]
            res += s1[::-1] + s2
            l += 2 * k

        return res
