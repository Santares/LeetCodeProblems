class StockSpanner:

    def __init__(self):
        self.stack = []
        self.record = {}

    def next(self, price: int) -> int:
        res = 1
        l = len(self.stack) - 1
        while l >= 0:
            x = self.stack[l]
            if x <= price:
                res += self.record[l]
                l -= self.record[l]
            else:
                break
        self.stack.append(price)
        self.record[len(self.stack) - 1] = res

        return res

    # faster
    def next2(self, price: int) -> int:
        res = 1
        l = len(self.stack) - 1
        while l >= 0:
            last = self.stack[l]
            x = last[0]
            if x <= price:
                res += last[1]
                l -= last[1]
            else:
                break
        self.stack.append([price, res])

        return res

    # faster
    def next3(self, price: int) -> int:
        res = 1
        l = len(self.stack) - 1
        while l >= 0:
            last = self.stack[l]
            x = last[0]
            if x <= price:
                res += last[1]
                l -= 1
                self.stack.pop()
            else:
                break
        self.stack.append([price, res])

        return res

    # online solution, faster
    def next4(self, price: int) -> int:
        # init our values
        stack, span = self.stack, 1

        while stack and stack[-1][0] <= price:
            span += stack[-1][1]
            stack.pop()
        stack.append((price, span))

        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

