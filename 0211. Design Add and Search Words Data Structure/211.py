class WordDictionary:

    def __init__(self):
        self.map = [None] * 26
        self.isEnd = False

    def addWord(self, word: str) -> None:
        if word:
            c = word[0]
            index = ord(c) - ord('a')
            if not self.map[index]:
                self.map[index] = WordDictionary()
            node = self.map[index]
            node.addWord(word[1:])
        else:
            self.isEnd = True

    def search(self, word: str) -> bool:
        if not word:
            return self.isEnd
        else:
            c = word[0]
            if c == '.':
                for node in self.map:
                    if node and node.search(word[1:]):
                        return True
                return False
            else:
                index = ord(c) - ord('a')
                if not self.map[index]:
                    return False
                else:
                    return self.map[index].search(word[1:])



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)