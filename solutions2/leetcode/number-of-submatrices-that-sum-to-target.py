class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if row - 1 >= 0:
                    matrix[row][col] += matrix[row - 1][col]
                if col - 1 >= 0:
                    matrix[row][col] += matrix[row][col-1]
                if row - 1 >= 0 and col - 1 >= 0:
                    matrix[row][col] -= matrix[row - 1][col - 1]
        # the above code is all about finding the prefix sum until that cell

        res = 0
        for row1 in range(rows):
            for row2 in range(row1, rows):
                count = defaultdict(int)
                count[0] = 1

                for c in range(cols):
                    curr_sum = matrix[row2][c] - (matrix[row1 - 1][c] if row1 > 0 else 0)
                    diff = curr_sum - target
                    res += count[diff]
                    count[curr_sum] += 1
        
        return res
                        
                
