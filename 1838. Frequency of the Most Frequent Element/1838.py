from typing import List


class Solution:
    # Too slow
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums = [float('-inf')] + nums + [float('inf')]
        res = 1
        for i in range(1, len(nums) - 1):
            total = 0
            count = 1
            l = i - 1
            while True:
                dif = nums[i] - nums[l]
                if dif + total <= k:
                    total += dif
                    count += 1
                    l -= 1
                else:
                    break
            res = max(res, count)

        return res

    # Slow, prefix sum + binary search
    def maxFrequency2(self, nums: List[int], k: int) -> int:
        nums.sort()
        prefixSums = [0]
        for x in nums:
            prefixSums.append(prefixSums[-1] + x)

        res = 1
        for i in range(len(nums) - 1, 0, -1):
            x = nums[i]

            left = 0
            right = i
            count = 0
            while left <= right:
                mid = (left + right) // 2
                total = (i - mid + 1) * x - (prefixSums[i + 1] - prefixSums[mid])
                if total <= k:
                    count = i + 1 - mid
                    right = mid - 1
                else:
                    left = mid + 1
            res = max(res, count)

        return res

    # Based on online solution. Sliding window
    def maxFrequency3(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        total = 0
        res = 1

        for r in range(1, len(nums)):
            total += (nums[r] - nums[r - 1]) * (r - l)
            while total > k:
                total -= nums[r] - nums[l]
                l += 1
            res = max(res, (r - l + 1))

        return res

if __name__ == '__main__':
    s = Solution()
    test1 = [9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966]
    test2 = 3056
    print(s.maxFrequency(test1, test2))
