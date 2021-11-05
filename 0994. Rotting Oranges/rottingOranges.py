from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def adjacent(i, j, grid, visit, m, n):
            temp = []
            if decay(i - 1, j, grid, visit, m, n) == 1:
                temp.append([i - 1, j])
            if decay(i + 1, j, grid, visit, m, n) == 1:
                temp.append([i + 1, j])
            if decay(i, j - 1, grid, visit, m, n) == 1:
                temp.append([i, j - 1])
            if decay(i, j + 1, grid, visit, m, n) == 1:
                temp.append([i, j + 1])

            return temp

        def decay(i, j, grid, visit, m, n):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            elif visit[i][j] == 0:
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    return 1
            return 0

        row = len(grid)
        column = len(grid[0])
        visit = [[0] * column] * row

        fresh = 0
        minute = 0
        rotten = []

        for i, r in enumerate(grid):
            for j, c in enumerate(grid[i]):
                if c == 2:
                    rotten.append([i, j])
                elif c == 1:
                    fresh += 1

        if len(rotten) == 0 and fresh == 0:
            return 0

        while len(rotten) != 0:
            temp = []
            for f in rotten:
                temp += adjacent(f[0], f[1], grid, visit, row, column)

            fresh -= len(temp)
            rotten = temp
            minute += 1

        if fresh != 0:
            return -1

        return minute - 1


# Time complexity: O(rows * cols) -> each cell is visited at least once
# Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue
# online solution
class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # number of rows
        rows = len(grid)
        if rows == 0:  # check if grid is empty
            return -1

        # number of columns
        cols = len(grid[0])

        # keep track of fresh oranges
        fresh_cnt = 0

        # queue with rotten oranges (for BFS)
        rotten = deque()

        # visit each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # add the rotten orange coordinates to the queue
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    # update fresh oranges count
                    fresh_cnt += 1

        # keep track of minutes passed.
        minutes_passed = 0

        # If there are rotten oranges in the queue and there are still fresh oranges in the grid keep looping
        while rotten and fresh_cnt > 0:

            # update the number of minutes passed
            # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
            minutes_passed += 1

            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                # visit all the adjacent cells
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    # calculate the coordinates of the adjacent cell
                    xx, yy = x + dx, y + dy
                    # ignore the cell if it is out of the grid boundary
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    # ignore the cell if it is empty '0' or visited before '2'
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue

                    # update the fresh oranges count
                    fresh_cnt -= 1

                    # mark the current fresh orange as rotten
                    grid[xx][yy] = 2

                    # add the current rotten to the queue
                    rotten.append((xx, yy))

        # return the number of minutes taken to make all the fresh oranges to be rotten
        # return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
        return minutes_passed if fresh_cnt == 0 else -1
