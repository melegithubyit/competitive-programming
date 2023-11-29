class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0 and matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True