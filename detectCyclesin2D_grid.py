class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        row, column = len(grid), len(grid[0])
        visited = [[False] * column for _ in range(row)]

        def dfs(x, y, prev_x, prev_y, target):
            visited[x][y] = True
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < row and 0 <= new_y < column and grid[new_x][new_y] == target:
                    if visited[new_x][new_y] and (new_x != prev_x or new_y != prev_y):
                        return True
                    if not visited[new_x][new_y] and dfs(new_x, new_y, x, y, target):
                        return True

            return False

        for i in range(row):
            for j in range(column):
                if not visited[i][j] and dfs(i, j, -1, -1, grid[i][j]):
                    return True

        return False



        