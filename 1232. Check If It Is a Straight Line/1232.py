import math
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        '''
        x1 - x2 / y1 - y2 = x2 - x3 / y2 - y3
        '''
        if len(coordinates) == 2:
            return True

        coordinates.sort()

        a = coordinates[0][0] - coordinates[1][0]
        b = coordinates[0][1] - coordinates[1][1]
        k = math.gcd(a, b)
        target = str(a // k) + '_' + str(b // k)

        for i in range(1, len(coordinates)):
            a = coordinates[i - 1][0] - coordinates[i][0]
            b = coordinates[i - 1][1] - coordinates[i][1]
            k = math.gcd(a, b)
            slope = str(a // k) + '_' + str(b // k)
            if slope != target:
                return False

        return True


    def checkStraightLine2(self, coordinates: List[List[int]]) -> bool:
        '''
        x1 - x2 / y1 - y2 = x2 - x3 / y2 - y3
        '''
        if len(coordinates) == 2:
            return True

        x = coordinates[0][0] - coordinates[1][0]
        y = coordinates[0][1] - coordinates[1][1]

        for i in range(2, len(coordinates)):
            x2 = coordinates[0][0] - coordinates[i][0]
            y2 = coordinates[0][1] - coordinates[i][1]
            if x * y2 - y * x2 != 0:
                return False

        return True