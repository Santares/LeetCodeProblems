# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            else:
                self.stack = self.stack[:-1] + top.getList()[::-1]
        return False


class NestedIterator2:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = []

        def dfs(nestedList):
            for item in nestedList:
                if item.isInteger():
                    self.queue.append(item.getInteger())
                else:
                    dfs(item.getList())

        dfs(nestedList)

    def next(self) -> int:
        if self.hasNext():
            return self.queue.pop(0)
        else:
            return -1

    def hasNext(self) -> bool:
        return len(self.queue) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

