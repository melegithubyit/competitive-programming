from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1] == 1:
            return -1
        dirs = [
            (1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
        queue = deque([(0, 0, 1)])

        while queue:
            i, j, length = queue.popleft()
            if i == j == n-1:
                return length
            for x, y in dirs:
                new_i, new_j = i+x, j+y

                if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] == 0:
                    grid[new_i][new_j] = 1
                    queue.append((new_i, new_j, length+1))
        return -1
