class MinStack:

    def __init__(self):
        self.stack = []
        self.minList = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minList.append(val)
        self.minList = sorted(self.minList)

    def pop(self) -> None:
        x = self.stack[-1]
        del self.stack[-1]
        self.minList.remove(x)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minList[0]


# faster
class MinStack2:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([val, val])
            return
        last_min = self.stack[-1][1]
        self.stack.append([val, min(val, last_min)])

    def pop(self) -> None:
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]