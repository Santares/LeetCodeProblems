class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = ''
        for i in range(len(num)-1, -1, -1):
          if int(num[i]) % 2 == 1:
            return num[:i+1]

        return res