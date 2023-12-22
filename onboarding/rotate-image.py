class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # transposed = list(map(list, zip(*matrix)))
        
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            left = 0
            right = len(matrix[i]) - 1

            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1

        
            



        