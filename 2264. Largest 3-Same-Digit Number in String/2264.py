class Solution:
    def largestGoodInteger(self, num: str) -> str:
        last = ''
        count = 0
        res = -1
        for i in range(len(num)):
            if last == '' or num[i] == last:
                count += 1
                if count == 3:
                    res = max(res, int(num[i]))
            else:
                count = 1
            last = num[i] 
            
        if res == -1:
            return ''
        else:
            return str(res) * 3
