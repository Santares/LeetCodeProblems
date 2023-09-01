from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        n = len(gas)
        if n == 1 and cost[0] <= gas[0]:
            return 0
        def helper(i):
            tank = 0
            for _ in range(n+1):
                tank = tank + gas[i] - cost[i]
                if tank < 0:
                    return i
                else:
                    i = (i+1)%n
            return (i-1)%n

        i = 0
        while i < n:
            if gas[i] > cost[i]:
                j = helper(i)
                if j == i:
                    return i
                elif j > i:
                    i = j
                else:
                    return -1
            else:
                i += 1
        return -1

    # Online solution, greedy
    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0
        for i in range(len(gas)):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1

        return start

if __name__ == '__main__':
    s = Solution()
    test1 = [1,2,3,4,5]
    test2 = [3,4,5,1,2]
    print(s.canCompleteCircuit(test1, test2))