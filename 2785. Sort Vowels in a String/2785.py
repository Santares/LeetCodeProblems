class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        pos = []
        chars = []
        s = list(s)
        for i, c in enumerate(s):
            if c in vowels:
                chars.append(c)
                pos.append(i)

        chars.sort()
        j = 0
        for i in pos:
            s[i] = chars[j]
            j += 1
        return ''.join(s)