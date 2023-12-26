class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        def move(position: list, directions: list, guard_set) -> None:
            posX, posY = position
            for i in directions:
                if i == 'up':
                    x, y = posX, posY
                    while x >= 0:
                        if grid[x][y] == '#' or (x, y) in guard_set:
                            break
                        grid[x][y] = 1
                        x -= 1

                if i == 'down':
                    x, y = posX, posY
                    while x < m:
                        if grid[x][y] == '#' or (x, y) in guard_set:
                            break
                        else:
                            grid[x][y] = 1
                        x += 1

                if i == 'right':
                    x, y = posX, posY
                    while y < n:
                        if grid[x][y] == '#' or (x, y) in guard_set:
                            break
                        else:
                            grid[x][y] = 1
                        y += 1

                if i == 'left':
                    x, y = posX, posY
                    while y >= 0:
                        if grid[x][y] == '#' or (x, y) in guard_set:
                            break
                        else:
                            grid[x][y] = 1
                        y -= 1

            
        
        directions = ['up', 'down', 'left', 'right']
        grid = [[0 for _ in range(n)] for _ in range(m)]

        guard_set = set()
        for row, col in guards:
            guard_set.add((row, col))

        for row,col in walls:
            grid[row][col] = '#'
        
        for row,col in guards:
            guard_set.remove((row,col))
            move((row, col), directions, guard_set)
            guard_set.add((row,col))

        count = 0
        for i in grid:
            for j in i:
                if j == 0:
                    count += 1
        
        return count