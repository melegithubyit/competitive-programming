class Solution:
    def bestClosingTime(self, customers: str) -> int:
        yesCount = customers.count('Y')
        noCount = 0
        pen = yesCount + noCount
        ans = 0

        for i in range(1, len(customers) + 1):
            if customers[i - 1] == 'Y':
                yesCount -= 1
            
            else:
                noCount += 1
            
            val = yesCount + noCount
            if val < pen:
                ans = i
                pen = val

        
        return ans

        