class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.combs = [i for i in range(combinationLength)]
        self.length = len(characters)
        self.nextExists = True
        if combinationLength > self.length:
            self.nextExists = False

    def next(self) -> str:
        res = ""
        for i in self.combs:
            res += self.chars[i]

        limit = self.length
        queue = []
        for j in range(len(self.combs) - 1, -1, -1):
            if self.combs[j] != limit - 1:
                self.combs[j] += 1
                for k in queue[::-1]:
                    self.combs[k] = self.combs[k - 1] + 1
                    queue.pop()

                break
            else:
                limit = self.combs[j]
                queue.append(j)
        if queue:
            self.nextExists = False

        return res

    def hasNext(self) -> bool:
        return self.nextExists

# online solution
class CombinationIterator2:

    def __init__(self, characters: str, combinationLength: int):
        from itertools import combinations
        self.c = sorted(list(combinations(characters, combinationLength)))

    def next(self) -> str:
        return ''.join(self.c.pop(0))

    def hasNext(self) -> bool:
        return len(self.c) > 0

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()