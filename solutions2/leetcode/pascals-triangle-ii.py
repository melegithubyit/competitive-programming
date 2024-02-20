class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        else:
            previous_row = self.getRow(rowIndex - 1)
            row = [1] * (rowIndex + 1)
            for i in range(1, rowIndex):
                row[i] = previous_row[i-1] + previous_row[i]
            
            return row