from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numSet = set()
        for i in nums:
            numSet.add(int(i))

        l = len(nums)

        def helper(last, index):
            if index == 0:
                return ""

            s1 = '0' + last
            if int(s1) not in numSet:
                return "0" * (index - 1) + s1

            s2 = '1' + last
            if int(s2) not in numSet:
                return "0" * (index - 1) + s2

            res = helper(s1, index - 1)
            if res == "":
                return helper(s2, index - 1)
            return res

        return helper("", l)

    # a little faster
    def findDifferentBinaryString2(self, nums: List[str]) -> str:
        numSet = set()
        for i in nums:
            numSet.add(int(i))

        l = len(nums)

        for i in range(1 << l):
            s = bin(i)[2:]
            if int(s) not in numSet:
                s = "0" * (l - len(s)) + s

                return s

        return ""


if __name__ == '__main__':
    solution = Solution()
    test = ["0000000111","0000001001","0000000100","0000000001","0000000010","1111111111","0000000101","0000000000","0000001000","0000000110"]
    test = ["00","01"]
    print(solution.findDifferentBinaryString2(test))
