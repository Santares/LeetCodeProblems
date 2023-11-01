class Solution:
    # memory limit exceeded
    def kthGrammar(self, n: int, k: int) -> int:
        nums = [0]
        map = {0: [0, 1], 1: [1, 0]}
        for i in range(n - 1):
            new = []
            for x in nums:
                new += map[x]
            nums = new

        return nums[k - 1]

    # Based on online solution
    def kthGrammar2(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k > 2 ** (n - 2):
            return 1 - self.kthGrammar(n - 1, k - 2 ** (n - 2))
        else:
            return self.kthGrammar(n - 1, k)



"""
0
0 1
01 10
0110 1001
0110 1001 1001 0110
01101001 10010110 10010110 01101001
"""