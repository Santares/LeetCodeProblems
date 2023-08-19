from collections import deque


class MyQueue:

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

        while prev:
            x = prev.pop()
            after.append(x)

        res = after.pop()

        while after:
            x = after.pop()
            prev.append(x)

        return res

    def peek(self) -> int:
        if self.q1:
            prev = self.q1
            after = self.q2
        else:
            prev = self.q2
            after = self.q1

        res = 0
        while prev:
            x = prev.pop()
            after.append(x)
            res = x

        while after:
            x = after.pop()
            prev.append(x)

        return res

    def empty(self) -> bool:
        return not (self.q1 or self.q2)


# Based on online solution
class MyQueue2:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if not self.q2:
            while self.q1:
                self.q2.append(self.q1.pop())

        return self.q2.pop()

    def peek(self) -> int:
        if not self.q2:
            while self.q1:
                self.q2.append(self.q1.pop())

        return self.q2[-1]

    def empty(self) -> bool:
        return not (self.q1 or self.q2)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
