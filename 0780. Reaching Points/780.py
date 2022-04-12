class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx

        if tx == sx and ty == sy:
            return True
        elif tx == sx:
            if ty > sy:
                return (ty - sy) % tx == 0
        elif ty == sy:
            if tx > sx:
                return (tx - sx) % ty == 0
        else:
            return False

    # online solution
    def reachingPoints1(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx != ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if tx == sx and ty == sy:
            return True
        elif tx == sx:
            return ty > sy and (ty - sy) % tx == 0
        elif ty == sy:
            return tx > sx and (tx - sx) % ty == 0
        else:
            return False

    # online solution
    def reachingPoints2(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while (sx < tx and sy < ty):
            if (ty > tx):
                ty %= tx
            else:
                tx %= ty
        if (sx > tx or sy > ty):
            return False
            # 又过了 while 又过了 if，说明 sx == tx 或者 sy == ty
        return (ty - sy) % sx == 0 if sx == tx else (tx - sx) % sy == 0;



if __name__ == '__main__':
    solution = Solution()

    test1 = 9
    test2 = 10
    test3 = 9
    test4 = 19
    print(solution.reachingPoints2(test1, test2, test3, test4))