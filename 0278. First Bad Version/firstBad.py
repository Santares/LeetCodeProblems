# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    bad = -1
    def setBadVersion(self, version):
        self.bad = version

    def isBadVersion(self, version):
        if version >= self.bad:
            return True
        return False

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if self.isBadVersion(mid):
                if not self.isBadVersion(mid - 1):
                    return mid
                else:
                    right = mid
            else:
                left = mid + 1
        return right

    def firstBadVersion2(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return right


if __name__ == '__main__':
    solution = Solution()
    test1 = 1
    test2 = 1
    test1 = 5
    test2 = 4

    solution.setBadVersion(test1)
    print(solution.firstBadVersion(test2))

