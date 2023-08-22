class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def helper(x):
            return chr(ord('A') + x)

        res = ""

        while columnNumber:
            x = (columnNumber - 1) % 26
            res = helper(x) + res
            columnNumber = (columnNumber - 1) // 26

        return res
