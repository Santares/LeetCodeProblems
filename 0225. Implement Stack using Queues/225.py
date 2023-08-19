from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        if self.q2:
            self.q2.append(x)
        else:
            self.q1.append(x)

    def pop(self) -> int:
        if self.q1:
            prev = self.q1
            after = self.q2
        else:
            prev = self.q2
            after = self.q1

        while len(prev) > 1:
            x = prev.popleft()
            after.append(x)

        return prev.pop()

    def top(self) -> int:
        if self.q1:
            prev = self.q1
            after = self.q2
        else:
            prev = self.q2
            after = self.q1

        while prev:
            x = prev.popleft()
            after.append(x)

        return x

    def empty(self) -> bool:
        return not (self.q1 or self.q2)


class MyStack2:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        length = len(self.q)
        for _ in range(length - 1):
            self.q.append(self.q.popleft())

        return self.q.popleft()

    def top(self) -> int:
        length = len(self.q)
        res = 0
        for _ in range(length):
            res = self.q.popleft()
            self.q.append(res)

        return res

    def empty(self) -> bool:
        return not self.q


class MyStack3:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        if self.q1:
            prev = self.q1
            after = self.q2
        else:
            prev = self.q2
            after = self.q1

        after.append(x)
        while prev:
            after.append(prev.popleft())

    def pop(self) -> int:
        if self.q1:
            return self.q1.popleft()
        else:
            return self.q2.popleft()

    def top(self) -> int:
        if self.q1:
            return self.q1[0]
        else:
            return self.q2[0]

    def empty(self) -> bool:
        return not (self.q1 or self.q2)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
