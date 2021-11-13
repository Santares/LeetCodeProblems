class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        stack = []

        for i in range(len(nums) - 1, 0, -1):
            x = nums[i-1]
            stack.append(nums[i])
            if x >= nums[i]:
                continue

            for j, y in enumerate(stack):
                if y > x:
                    stack[j] = nums[i-1]
                    nums[i-1] = y
                    nums[i:] = sorted(stack)

                    num = int(''.join(nums))
                    if num > (1 << 31) - 1:
                        return -1
                    return num

        return -1

    # online solution
    def nextGreaterElement2(self, n: int) -> int:
        nums = list(str(n))
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                l, r = i-1, i
                while r < len(nums) - 1 and nums[r+1] > nums[l]:
                    r += 1
                nums[l], nums[r] = nums[r], nums[l]
                nums[l+1:] = nums[l+1:][::-1]
                ans = int(''.join(nums))
                return ans if -2**31<=ans<=2**31-1 else -1
        return -1

if __name__ == '__main__':
    solution = Solution()
    # test = 2147483476
    test = 12
    print(solution.nextGreaterElement(test))
