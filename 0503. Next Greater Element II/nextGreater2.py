from typing import List

class Solution:
    # slow
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        queue = []
        l = len(nums)
        res = [-1] * len(nums)

        for i in range(len(nums) * 2):
            x = nums[i % l]
            while queue:
                if x > nums[queue[-1]]:
                    res[queue[-1]] = x
                    queue.pop()
                else:
                    break
            queue.append(i % l)

        return res

    # online solution, faster
    def nextGreaterElements2(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                result[stack.pop()] = x
            stack.append(i)
        for x in nums:
            while stack and nums[stack[-1]] < x:
                result[stack.pop()] = x
        return result

    # 2023/08/24
    def nextGreaterElements3(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [-1] * (l * 2)
        queue = deque()

        nums = nums + nums
        for i, x in enumerate(nums):
            while queue and nums[queue[-1]] < x:
                res[queue[-1]] = x
                queue.pop()
            queue.append(i)

        return res[:l]

if __name__ == '__main__':
    solution = Solution()
    test = [1,2,1]
    print(solution.nextGreaterElements(test))
