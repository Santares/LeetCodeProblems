from typing import List


class Solution:
    # Too slow
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == "":
            return True
        i = 1
        res = []
        while i <= len(s):
            word = s[:i]
            if word not in wordDict:
                i += 1
            else:
                res.append(i)
                i += 1

        for j in res[::-1]:
            if self.wordBreak(s[j:], wordDict):
                return True
        return False

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        memory = {"": True}

        def helper(s):
            if s in memory:
                return memory[s]
            res = False
            for word in wordDict:
                l = len(word)
                if s[:l] == word:
                    if helper(s[l:]):
                        res = True
                        break
            memory[s] = res
            return res

        return helper(s)

if __name__ == "__main__":
    solution = Solution()

    # test1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    # test2 = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    test1 = "leetcode"
    test2 = ["leet", "code"]
    print(solution.wordBreak2(test1, test2))
