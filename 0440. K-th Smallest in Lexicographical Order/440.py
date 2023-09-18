class Solution:
    # Memory limit exceeded
    def findKthNumber(self, n: int, k: int) -> int:
        nums = []
        for i in range(1, n+1):
            nums.append(str(i))
        nums.sort()
        return int(nums[k-1])

    # Based on online solution. Trie
    def findKthNumber2(self, n: int, k: int) -> int:
        def getCount(prefix, n):
            cur = prefix
            nxt = cur + 1
            count = 0
            while cur <= n:
                num = min(nxt, n + 1) - cur
                count += num
                cur *= 10
                nxt *= 10
            return count

        index = 1
        prefix = 1
        while index < k:
            count = getCount(prefix, n)
            if index + count > k:
                prefix *= 10
                index += 1
            else:
                index += count
                prefix += 1

        return prefix



if __name__ == '__main__':
    s = Solution()
    test1 = 13
    test2 = 2

    print(s.findKthNumber(test1, test2))
