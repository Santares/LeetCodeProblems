from typing import List
class Solution:
    # slow
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        record = [-1] * len(nums2)
        res = []

        for i in range(len(nums2)):
            while (stack):
                if nums2[i] > nums2[stack[-1]]:
                    record[stack[-1]] = nums2[i]
                    stack.pop()
                else:
                    break
            stack.append(i)

        for x in nums1:
            for j in range(len(nums2)):
                if x == nums2[j]:
                    res.append(record[j])
                    break

        return res

    # brutal force solution, slowest
    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for x in nums1:
            for i in range(len(nums2)):
                if x == nums2[i]:
                    res.append(-1)
                    for y in nums2[i:]:
                        if y > x:
                            res[-1] = y
                            break

        return res

    # use hash map, much faster
    def nextGreaterElement3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        record = {}
        res = []

        for i in range(len(nums2)):
            while (stack):
                if nums2[i] > nums2[stack[-1]]:
                    record[nums2[stack[-1]]] = nums2[i]
                    stack.pop()
                else:
                    break
            stack.append(i)

        for x in nums1:
            if x in record:
                res.append(record[x])
            else:
                res.append(-1)

        return res

    # online solution, similar to 3
    def nextGreaterElement4(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nxt_greatest = {}
        stack = []
        for n in nums2:
            while (len(stack) and stack[-1] < n):
                nxt_greatest[stack.pop()] = n
            stack.append(n)
        for i in range(len(nums1)):
            nums1[i] = nxt_greatest.get(nums1[i], -1)
        return nums1


if __name__ == '__main__':
    solution = Solution()
    test1 = [4,1,2]
    test2 = [1,3,4,2]
    print(solution.nextGreaterElement2(test1, test2))