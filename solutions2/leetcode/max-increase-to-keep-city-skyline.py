class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        transposed = list(map(list, zip(*grid)))
        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                stored_val = min(max(grid[row]), max(transposed[col]))
                count += abs(stored_val - grid[row][col])

        return count

        
