class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        n = len(self.matrix)
        m = len(self.matrix[0])

        for row in range(n):
            for col in range(m):
                if row - 1 >= 0:
                    self.matrix[row][col] += self.matrix[row - 1][col]
                if col - 1 >= 0:
                    self.matrix[row][col] += self.matrix[row][col - 1]
                if col - 1 >= 0 and row - 1 >= 0:
                    self.matrix[row][col] -= self.matrix[row - 1][col - 1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        def computer(row, col):
            return self.matrix[row][col]

        max_sum = computer(row2, col2)
        sum1 = sum2 = sum3 = 0

        if row1 - 1 >= 0:
            sum1 = computer(row1 - 1, col2)
        
        if col1 - 1 >= 0:
            sum2 = computer(row2, col1 - 1)

        if row1 - 1 >= 0 and col1 - 1 >= 0:
            sum3 = computer(row1 - 1, col1 - 1)

        return max_sum - sum1 - sum2 + sum3



        

        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)