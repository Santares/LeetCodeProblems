class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        a = num % 10
        if a == 0:
            pass
        elif a < 4:
            res += ['I' * a]
        elif a == 4:
            res += ["IV"]
        elif a == 5:
            res.append("V")
        elif a < 9:
            res.append("V" + 'I' * (a - 5))
        else:
            res.append("IX")

        num = num // 10
        if num == 0:
            pass
        else:
            a = num % 10
            if a == 0:
                pass
            elif a < 4:
                res += ['X' * a]
            elif a == 4:
                res += ["XL"]
            elif a == 5:
                res.append("L")
            elif a < 9:
                res.append("L" + 'X' * (a - 5))
            else:
                res.append("XC")

        num = num // 10
        if num == 0:
            pass
        else:
            a = num % 10
            if a == 0:
                pass
            elif a < 4:
                res += ['C' * a]
            elif a == 4:
                res += ["CD"]
            elif a == 5:
                res.append("D")
            elif a < 9:
                res.append("D" + 'C' * (a - 5))
            else:
                res.append("CM")

        num = num // 10
        res.append("M" * num)

        return "".join(reversed(res))

    # faster
    def intToRoman2(self, num: int) -> str:
        res = ""
        ones = num % 10
        tens = num // 10 % 10
        hundreds = num // 100 % 10
        thousands = num // 1000 % 10

        res += "M" * thousands

        if hundreds:
            if hundreds < 4:
                res += 'C' * hundreds
            elif hundreds == 4:
                res += "CD"
            elif hundreds == 5:
                res += "D"
            elif hundreds < 9:
                res += "D" + 'C' * (hundreds - 5)
            else:
                res += "CM"

        if tens:
            if tens < 4:
                res += 'X' * tens
            elif tens == 4:
                res += "XL"
            elif tens == 5:
                res += "L"
            elif tens < 9:
                res += "L" + 'X' * (tens - 5)
            else:
                res += "XC"

        if ones:
            if ones < 4:
                res += 'I' * ones
            elif ones == 4:
                res += "IV"
            elif ones == 5:
                res += "V"
            elif ones < 9:
                res += "V" + 'I' * (ones - 5)
            else:
                res += "IX"

        return res

    # 2023/09/18
    def intToRoman3(self, num: int) -> str:
        symbols = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

        t = 0
        res = ""
        while num != 0:
            d = num % 10
            cur = ""
            if d * (10 ** t) in symbols:
                cur = symbols[d * (10 ** t)]
            elif d < 4:
                cur = d * symbols[(10 ** t)]
            elif d == 4:
                cur = symbols[(10 ** t)] + symbols[5 * (10 ** t)]
            elif d < 9:
                cur = symbols[5 * (10 ** t)] + (d - 5) * symbols[(10 ** t)]
            else:  # d == 9
                cur = symbols[10 ** t] + symbols[10 ** (t + 1)]

            res = cur + res
            num = num // 10
            t += 1

        return res
