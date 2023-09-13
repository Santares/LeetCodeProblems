from collections import deque, defaultdict
from typing import List


class Solution:
    # Memory limit exceeded
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordDict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                wordDict[key].append(word)

        queue = deque([[beginWord]])
        visited = set()
        res = []
        found = False
        while queue and not found:
            subVisited = set()
            for _ in range(len(queue)):
                path = queue.popleft()
                word = path[-1]
                for i in range(len(word)):
                    key = word[:i] + '*' + word[i + 1:]
                    for nxt in wordDict[key]:
                        if nxt == endWord:
                            found = True
                            res.append(path + [nxt])
                        elif nxt not in visited:
                            queue.append(path + [nxt])
                            subVisited.add(nxt)
            visited = visited.union(subVisited)

        return res

    # too slow
    def findLadders2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordDict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                wordDict[key].append(word)

        def helper(beginWord: str, endWord: str) -> int:
            queue = deque([beginWord])
            count = 1
            visited = set()
            while queue:
                for _ in range(len(queue)):
                    word = queue.popleft()
                    for i in range(len(word)):
                        key = word[:i] + '*' + word[i + 1:]
                        for nxt in wordDict[key]:
                            if nxt == endWord:
                                return count + 1
                            elif nxt not in visited:
                                queue.append(nxt)
                                visited.add(nxt)
                count += 1

            return 0

        print("hello")
        level = helper(beginWord, endWord)
        res = []

        def dfs(cur):
            if len(cur) == level:
                return
            word = cur[-1]
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                for nxt in wordDict[key]:
                    if nxt == endWord:
                        res.append(cur + [nxt])
                    elif nxt not in cur:
                        cur.append(nxt)
                        dfs(cur)
                        cur.pop()

        dfs([beginWord])

        return res

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordDict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                wordDict[key].append(word)

        queue = deque([beginWord])
        count = 1
        visited = {beginWord}
        res = []
        found = False
        record = []
        while queue and not found:
            record.append(list(queue))
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    key = word[:i] + '*' + word[i + 1:]
                    for nxt in wordDict[key]:
                        if nxt == endWord:
                            found = True
                        elif nxt not in visited:
                            queue.append(nxt)
                            visited.add(nxt)
            count += 1

        res = []

        def isConnect(word1, word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1

            return count == 1

        def helper(word, level, step):
            if word == beginWord:
                res.append(step[::-1])
                return
            if level < 0:
                return

            for word2 in record[level]:
                if isConnect(word, word2):
                    helper(word2, level - 1, step + [word2])

        if found:
            helper(endWord, count - 2, [endWord])

        return res

if __name__ == '__main__':
    s = Solution()
    test1 = "red"
    test2 = "tax"
    test3 = ["ted","tex","red","tax","tad","den","rex","pee"]
    # test2 = "oecij"
    # test1 = "ymain"
    # test3 = ["ymann", "yycrj", "oecij", "ymcnj", "yzcrj", "yycij", "xecij", "yecij", "ymanj", "yzcnj", "ymain"]
    # test1 = "hit"
    # test2 = "cog"
    # test3 = ["hot", "dot", "dog", "lot", "log", "cog"]
    # test1 = "aaaaa"
    # test2 = "ggggg"
    # test3 = ["aaaaa","caaaa","cbaaa","daaaa","dbaaa","eaaaa","ebaaa","faaaa","fbaaa","gaaaa","gbaaa","haaaa","hbaaa","iaaaa","ibaaa","jaaaa","jbaaa","kaaaa","kbaaa","laaaa","lbaaa","maaaa","mbaaa","naaaa","nbaaa","oaaaa","obaaa","paaaa","pbaaa","bbaaa","bbcaa","bbcba","bbdaa","bbdba","bbeaa","bbeba","bbfaa","bbfba","bbgaa","bbgba","bbhaa","bbhba","bbiaa","bbiba","bbjaa","bbjba","bbkaa","bbkba","bblaa","bblba","bbmaa","bbmba","bbnaa","bbnba","bboaa","bboba","bbpaa","bbpba","bbbba","abbba","acbba","dbbba","dcbba","ebbba","ecbba","fbbba","fcbba","gbbba","gcbba","hbbba","hcbba","ibbba","icbba","jbbba","jcbba","kbbba","kcbba","lbbba","lcbba","mbbba","mcbba","nbbba","ncbba","obbba","ocbba","pbbba","pcbba","ccbba","ccaba","ccaca","ccdba","ccdca","cceba","cceca","ccfba","ccfca","ccgba","ccgca","cchba","cchca","cciba","ccica","ccjba","ccjca","cckba","cckca","cclba","cclca","ccmba","ccmca","ccnba","ccnca","ccoba","ccoca","ccpba","ccpca","cccca","accca","adcca","bccca","bdcca","eccca","edcca","fccca","fdcca","gccca","gdcca","hccca","hdcca","iccca","idcca","jccca","jdcca","kccca","kdcca","lccca","ldcca","mccca","mdcca","nccca","ndcca","occca","odcca","pccca","pdcca","ddcca","ddaca","ddada","ddbca","ddbda","ddeca","ddeda","ddfca","ddfda","ddgca","ddgda","ddhca","ddhda","ddica","ddida","ddjca","ddjda","ddkca","ddkda","ddlca","ddlda","ddmca","ddmda","ddnca","ddnda","ddoca","ddoda","ddpca","ddpda","dddda","addda","aedda","bddda","bedda","cddda","cedda","fddda","fedda","gddda","gedda","hddda","hedda","iddda","iedda","jddda","jedda","kddda","kedda","lddda","ledda","mddda","medda","nddda","nedda","oddda","oedda","pddda","pedda","eedda","eeada","eeaea","eebda","eebea","eecda","eecea","eefda","eefea","eegda","eegea","eehda","eehea","eeida","eeiea","eejda","eejea","eekda","eekea","eelda","eelea","eemda","eemea","eenda","eenea","eeoda","eeoea","eepda","eepea","eeeea","ggggg","agggg","ahggg","bgggg","bhggg","cgggg","chggg","dgggg","dhggg","egggg","ehggg","fgggg","fhggg","igggg","ihggg","jgggg","jhggg","kgggg","khggg","lgggg","lhggg","mgggg","mhggg","ngggg","nhggg","ogggg","ohggg","pgggg","phggg","hhggg","hhagg","hhahg","hhbgg","hhbhg","hhcgg","hhchg","hhdgg","hhdhg","hhegg","hhehg","hhfgg","hhfhg","hhigg","hhihg","hhjgg","hhjhg","hhkgg","hhkhg","hhlgg","hhlhg","hhmgg","hhmhg","hhngg","hhnhg","hhogg","hhohg","hhpgg","hhphg","hhhhg","ahhhg","aihhg","bhhhg","bihhg","chhhg","cihhg","dhhhg","dihhg","ehhhg","eihhg","fhhhg","fihhg","ghhhg","gihhg","jhhhg","jihhg","khhhg","kihhg","lhhhg","lihhg","mhhhg","mihhg","nhhhg","nihhg","ohhhg","oihhg","phhhg","pihhg","iihhg","iiahg","iiaig","iibhg","iibig","iichg","iicig","iidhg","iidig","iiehg","iieig","iifhg","iifig","iighg","iigig","iijhg","iijig","iikhg","iikig","iilhg","iilig","iimhg","iimig","iinhg","iinig","iiohg","iioig","iiphg","iipig","iiiig","aiiig","ajiig","biiig","bjiig","ciiig","cjiig","diiig","djiig","eiiig","ejiig","fiiig","fjiig","giiig","gjiig","hiiig","hjiig","kiiig","kjiig","liiig","ljiig","miiig","mjiig","niiig","njiig","oiiig","ojiig","piiig","pjiig","jjiig","jjaig","jjajg","jjbig","jjbjg","jjcig","jjcjg","jjdig","jjdjg","jjeig","jjejg","jjfig","jjfjg","jjgig","jjgjg","jjhig","jjhjg","jjkig","jjkjg","jjlig","jjljg","jjmig","jjmjg","jjnig","jjnjg","jjoig","jjojg","jjpig","jjpjg","jjjjg","ajjjg","akjjg","bjjjg","bkjjg","cjjjg","ckjjg","djjjg","dkjjg","ejjjg","ekjjg","fjjjg","fkjjg","gjjjg","gkjjg","hjjjg","hkjjg","ijjjg","ikjjg","ljjjg","lkjjg","mjjjg","mkjjg","njjjg","nkjjg","ojjjg","okjjg","pjjjg","pkjjg","kkjjg","kkajg","kkakg","kkbjg","kkbkg","kkcjg","kkckg","kkdjg","kkdkg","kkejg","kkekg","kkfjg","kkfkg","kkgjg","kkgkg","kkhjg","kkhkg","kkijg","kkikg","kkljg","kklkg","kkmjg","kkmkg","kknjg","kknkg","kkojg","kkokg","kkpjg","kkpkg","kkkkg","ggggx","gggxx","ggxxx","gxxxx","xxxxx","xxxxy","xxxyy","xxyyy","xyyyy","yyyyy","yyyyw","yyyww","yywww","ywwww","wwwww","wwvww","wvvww","vvvww","vvvwz","avvwz","aavwz","aaawz","aaaaz"]

    print(s.findLadders3(test1, test2, test3))
