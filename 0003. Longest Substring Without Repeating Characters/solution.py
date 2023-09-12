from collections import defaultdict


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

    # 2023/09/11
    def lengthOfLongestSubstring2(self, s: str) -> int:
        visited = defaultdict(int)
        res = 0
        left = 0
        for right in range(len(s)):
            c = s[right]
            if visited[c] == 0:
                visited[c] += 1
                res = max(res, right - left + 1)
            else:
                while True:
                    l = s[left]
                    left += 1
                    if l == c:
                        break
                    else:
                        visited[l] -= 1

        return res
