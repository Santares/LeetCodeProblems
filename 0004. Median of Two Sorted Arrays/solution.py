from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        m = (l1 + l2) / 2
        res = 0

        j = 0
        k = 0
        while 1 <= m:
            if j >= l1:
                res = nums2[k]
                k += 1
            elif k >= l2:
                res = nums1[j]
                j += 1
            elif nums1[j] <= nums2[k]:
                res = nums1[j]
                j += 1
            else:
                res = nums2[k]
                k += 1
            m -= 1

        if m == 0:
            if j >= l1:
                res = (res + nums2[k]) / 2
                k += 1
            elif k >= l2:
                res = (res + nums1[j]) / 2
            else:
                res = (res + min(nums1[j], nums2[k])) / 2
        else:
            if j >= l1:
                res = nums2[k]
                k += 1
            elif k >= l2:
                res = nums1[j]
            else:
                res = min(nums1[j], nums2[k])

        return res

    # slight improvement
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        m = (l1 + l2) / 2
        temp = []
        res = 0

        j = 0
        k = 0
        while True:
            if j >= l1 and k >= l2:
                break;
            if j >= l1:
                temp.append(nums2[k])
                k += 1
            elif k >= l2:
                temp.append(nums1[j])
                j += 1
            elif nums1[j] <= nums2[k]:
                temp.append(nums1[j])
                j += 1
            else:
                temp.append(nums2[k])
                k += 1

        if m % 1 != 0:
            res = temp[int(m)]
        else:
            res = (temp[int(m) - 1] + temp[int(m)]) / 2

        return res

    # online solution
    def findMedianSortedArrays3(self, nums1: List[int], nums2: List[int]) -> float:
        completed_array = nums1 + nums2
        completed_array.sort()

        l = len(completed_array)

        if l % 2 == 1:
            return completed_array[int(l / 2)]

        else:
            i = int(l / 2) - 1
            return (completed_array[i] + completed_array[i + 1]) / 2

if __name__ == '__main__':
    test1 = [1, 3]
    test2 = [2]
    test1 = [1, 2]
    test2 = [3, 4]
    solution = Solution()
    result = solution.findMedianSortedArrays(test1, test2)
    print(result)
