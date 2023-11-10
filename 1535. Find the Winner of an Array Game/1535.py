from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)

        for i in range(n):
            num = arr[i]
            j = 0
            if i > 0:
                x = arr[i - 1]
                if x < num:
                    j += 1

            z = 1
            while j < k:
                index = (i + z) % n
                if arr[index] < num:
                    j += 1
                    z += 1
                else:
                    break

            if j == k:
                return num

    # Another version of solution 1
    def getWinner2(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)

        for i in range(n):
            num = arr[i]
            count = 0
            if i > 0 and arr[i - 1] < num:
                count += 1
            for j in range(1, k + 1):
                if arr[(i + j) % n] < num:
                    count += 1
                else:
                    break
            if count >= k:
                return num


if __name__ == '__main__':
    s = Solution()
    test1 = [2,1,3,5,4,6,7]
    test2 = 2
    test1 = [3,1,2,4,5,6,7]
    test2 = 6
    print(s.getWinner2(test1, test2))