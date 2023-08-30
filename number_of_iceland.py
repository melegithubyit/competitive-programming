class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= num_rows or col >= num_cols or grid[row][col] != '1':
                return

            grid[row][col] = '0'
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1':
                    num_islands += 1
                    dfs(row, col)

        return num_islands
