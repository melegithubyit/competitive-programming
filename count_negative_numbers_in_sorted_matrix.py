class Solution:
    def countNegatives(self, grid) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        r = rows - 1
        c = 0

        while r >= 0 and c < cols:
            if grid[r][c] < 0:
                count += cols - c
                r -= 1
            else:
                c += 1

        return count
