class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ""
        if numerator < 0 and denominator > 0:
            res += "-"
            numerator *= -1
        elif numerator < 0 and denominator < 0:
            numerator *= -1
            denominator *= -1
        elif numerator > 0 and denominator < 0:
            res += "-"
            denominator *= -1

        res += str(numerator // denominator)

        rem = numerator % denominator
        if rem == 0:
            return res

        res += "."
        rems = {rem: 0}
        temp = []
        count = 1
        while rem != 0:
            rem *= 10

            temp.append(rem // denominator)
            rem %= denominator

            if rem in rems:
                res += "".join(str(x) for x in temp[:rems[rem]])
                res += "(" + "".join(str(x) for x in temp[rems[rem]:]) + ")"
                return res
            else:
                rems[rem] = count
                count += 1

        res += "".join(str(x) for x in temp)
        return res

    # online solution
    def fractionToDecimal2(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        flag = '-' if (numerator < 0) != (denominator < 0) else ''
        numerator, denominator = abs(numerator), abs(denominator)
        res = flag + str(int(numerator/ denominator))
        part = numerator % denominator
        if part !=0:
            res = res + '.'
        record = {}
        while part > 0:
            record[part] = len(res)
            part = part * 10
            sub_q = part // denominator
            part = part % denominator
            res = res + str(sub_q)
            if part in record:
                return res[:record[part]] + '(' + res[record[part]:] + ')'
        return res

if __name__ == '__main__':
    solution = Solution()
    test1 = 1
    test2 = 2
    print(solution.fractionToDecimal(test1, test2))
