class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        numList = []
        for i in range(numRows):
            numList.append([])
        order = 1
        index = 0
        for c in s:
            if index == 0:
                order = 1
            elif index == numRows - 1:
                order = -1

            numList[index].append(c)

            index += order

        res = []
        for l in numList:
            res += l

        return "".join(res)


    # online solution, not very fast
    def convert2(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = [''] * numRows
        row, index = 0, 0
        for char in s:
            arr[row] += char
            if row == 0:
                index = 1
            elif row == numRows - 1:
                index = -1
            row += index

        return ''.join(arr)

if __name__ == '__main__':
    test1 = "PAYPALISHIRING"
    test2 = 3
    solution = Solution()
    print(solution.convert(test1, test2))