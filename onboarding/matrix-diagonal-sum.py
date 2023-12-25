class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        def check(x):
            return (x-1) // 2

        n = len(mat)
        curr_col = curr_row = 0
        last_row = 0
        last_col = n-1
        _sum = 0

        while curr_col < n and curr_row < n:
            _sum += (mat[curr_row][curr_col])
            curr_row += 1
            curr_col += 1
        
        while last_row < n and last_col >= 0:
            _sum += (mat[last_row][last_col])
            last_row += 1
            last_col -= 1

        if n % 2 == 0:
            return _sum
        else:
            return _sum - (mat[check(n)][check(n)])
            

        


