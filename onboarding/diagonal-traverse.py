class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        curr_col = 0
        curr_row = 0

        max_row =  len(mat) -1
        max_col =len(mat[0]) - 1

        direction = 'UR'
        result = []

        while curr_row <= max_row and curr_col <= max_col:

            if direction == 'UR':
                result.append(mat[curr_row][curr_col])

                while curr_row > 0 and curr_col < max_col:
                    curr_row -= 1
                    curr_col += 1
                    result.append(mat[curr_row][curr_col])
                
                if curr_col == max_col:
                    direction = 'D'
                else:
                    direction = 'R'
                
            if direction == 'DL':
                result.append(mat[curr_row][curr_col])

                while curr_row < max_row and curr_col > 0:
                    curr_col -= 1
                    curr_row += 1
                    result.append(mat[curr_row][curr_col])
                
                if curr_row == max_row:
                    direction = 'R'
                else:
                    direction = 'D'
            
            if direction == 'D':
                curr_row += 1
                if curr_col == max_col:
                    direction = 'DL'
                else:
                    direction = 'UR'

            if direction == 'R':
                curr_col += 1
                if curr_row == max_row:
                    direction = 'UR'
                else:
                    direction = 'DL'

        return result
            




        