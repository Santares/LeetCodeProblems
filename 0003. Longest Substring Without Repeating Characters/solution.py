class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDic = {}
        maxLen = 0
        index = 0
        lastIndex = 0
        for c in s:
            if c not in charDic or charDic[c] < lastIndex:
                charDic[c] = index
                index += 1
            else:
                maxLen = max(maxLen, index - lastIndex)
                lastIndex = charDic[c] + 1
                charDic[c] = index
                index += 1

        maxLen = max(maxLen, index - lastIndex)

        return maxLen

