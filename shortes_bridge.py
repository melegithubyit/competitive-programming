from collections import deque
class Solution:
    def shortestBridge(self, grid):
        n = len(grid)
        queue = deque([])

        def dfs(r, c):
            grid[r][c] = -1
            queue.append((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if nr in range(n) and nc in range(n) and grid[nr][nc] == 1:
                    dfs(nr, nc)

        row, col = -1, -1
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    row, col = r, c
                    break

        dfs(row, col)
        bridgeLength = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(n) and nc in range(n):
                        if grid[nr][nc] == 1:
                            return bridgeLength

                        elif grid[nr][nc] == 0:
                            queue.append((nr, nc))
                            grid[nr][nc] = -1

            bridgeLength += 1

        return bridgeLength
