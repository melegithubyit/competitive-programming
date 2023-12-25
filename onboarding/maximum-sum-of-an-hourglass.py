class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        horizontal_iter = len(grid[0]) - 2
        vertical_iter = len(grid) - 2
        max_sum = float('-inf')

        for i in range(vertical_iter):
            for j in range(horizontal_iter):
                curr_sum = sum(grid[i][j:j+3]) + grid[i+1][j+1] + sum(grid[i+2][j:j+3])
                max_sum = max(max_sum, curr_sum)

        
        return max_sum


        


        