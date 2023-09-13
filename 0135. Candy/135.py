from typing import List


class Solution:
    # Acceptable, but slow
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        def update(i):
            if i < 0 or i >= n:
                return
            else:
                updated = False
                for j in [1, -1]:
                    if 0 <= i + j < n and ratings[i] > ratings[i + j]:
                        if candies[i] <= candies[i + j]:
                            updated = True
                            candies[i] = candies[i + j] + 1
                if updated:
                    update(i + 1)
                    update(i - 1)

        for i in range(n):
            update(i)

        return sum(candies)

    # Based on online solution, much faster
    def candy2(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)


if __name__ == '__main__':
    s = Solution()
    test1 = [2,1,0]
    print(s.candy(test1))