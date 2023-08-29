from collections import Counter


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        count = Counter(customers)
        penalty = count['Y']
        res = -1
        minP = penalty
        for i, x in enumerate(customers):
            if x == 'Y':
                penalty -= 1
                if penalty < minP:
                    minP = penalty
                    res = i
            else:
                penalty += 1

        return res + 1

    # Based on online solution, improved version of solution1
    def bestClosingTime2(self, customers: str) -> int:
        penalty = 0
        res = 0
        minP = penalty
        for i, x in enumerate(customers, 1):
            if x == 'Y':
                penalty -= 1
                if penalty < minP:
                    minP = penalty
                    res = i
            else:
                penalty += 1

        return res
