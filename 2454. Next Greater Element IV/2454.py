from typing import List


class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        stack1 = []
        stack2 = []
        res = [-1] * len(nums)
        for i in range(len(nums)):
            x = nums[i]
            while stack2 and nums[stack2[-1]] < x:
                res[stack2.pop()] = x
            if stack1:
                j = len(stack1)-1
                while j >= 0 and nums[stack1[j]] < x:
                    j -= 1
                stack2 += stack1[j+1:]
                del stack1[j+1:]
            stack1.append(i)
        return res

    # online solution
    def secondGreaterElement2(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        s, ss = [], []
        for i, x in enumerate(nums):
            while ss and nums[ss[-1]] < x:
                ans[ss.pop()] = x
            buff = []
            while s and nums[s[-1]] < x:
                buff.append(s.pop())
            while buff:
                ss.append(buff.pop())
            s.append(i)
        return ans


if __name__ == '__main__':
    s = Solution()
    test1 = [2,4,0,9,6]
    test1 = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
    print(s.secondGreaterElement(test1))