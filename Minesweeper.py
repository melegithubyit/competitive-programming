class Solution:
    def updateBoard(self, board, click):
        m = len(board[0])
        n = len(board)
        visited = set()

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        queue = [click]

        while queue:
            i, j = queue.pop()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            num = 0
            temp = []
            for s in directions:
                i1, j1 = i + s[0], j + s[1]
                if i1 >= 0 and i1 < n and j1 >= 0 and j1 < m:
                    if board[i1][j1] == 'M':
                        num += 1
                    elif board[i1][j1] == 'E':
                        temp.append((i1, j1))

            if num:
                board[i][j] = str(num)
            else:
                board[i][j] = 'B'
                queue += temp

        return board
