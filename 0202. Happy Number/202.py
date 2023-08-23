class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1 and n not in visited:
            visited.add(n)
            res = 0
            while n != 0:
                res += (n % 10) ** 2
                n = n // 10
            n = res

        return n == 1
