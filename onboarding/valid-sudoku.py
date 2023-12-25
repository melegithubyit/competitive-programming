class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        matrix = defaultdict(set)

        for row in range(9):
            for col in range(9):
                cell = board[row][col]

                if cell == '.':
                    continue

                if cell in rows[row] or cell in cols[col] or cell in matrix[(row//3, col//3)]:
                    return False

                rows[row].add(cell)
                cols[col].add(cell)

                matrix[(row//3, col//3)].add(cell)

        return True




        