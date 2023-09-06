from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        res = 0

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1
                    if i > 0 and j > 0 and nums1[i - 1] == nums2[j - 1]:
                        dp[i][j] += dp[i - 1][j - 1]

                    res = max(res, dp[i][j])

        return res

    def findLength2(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        res = 0

        dp = [0] * n
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[j] = 1
                    if i > 0 and j > 0 and nums1[i - 1] == nums2[j - 1]:
                        dp[j] += dp[j - 1]

                    res = max(res, dp[j])

        return res


if __name__ == '__main__':
    s = Solution()

    test1 = [1,5,3,2,1]
    test2 = [3,5,2,4,7]
    print(s.findLength(test1, test2))
    print(s.findLength2(test1, test2))