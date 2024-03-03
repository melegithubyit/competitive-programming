class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def is_safe(board, row, col):
            
            for prev_row in range(row):
                if board[prev_row][col] == 'Q':
                    return False

                if col - (row - prev_row) >= 0 and board[prev_row][col - (row - prev_row)] == 'Q':
                    return False

                if col + (row - prev_row) < n and board[prev_row][col + (row - prev_row)] == 'Q':
                    return False

            return True

        self.ans = 0
        
        def backtrack(row):

            if row == n:
                self.ans += 1
                return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'

        board = []
        
        for _ in range(n):
            board.append(['.' for _ in range(n)])       

        result = []
        backtrack(0)

        return self.ans
