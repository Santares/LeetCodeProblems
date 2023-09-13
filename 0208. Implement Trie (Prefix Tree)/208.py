# Based on online solution
class Trie:

    def __init__(self):
        self.isEnd = False
        self.next = {}

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.next:
                node.next[c] = Trie()
            node = node.next[c]

        node.isEnd = True
        return

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if c not in node.next:
                return False
            else:
                node = node.next[c]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if c not in node.next:
                return False
            else:
                node = node.next[c]
        return True
