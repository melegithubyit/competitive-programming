class Solution:
    def totalMoney(self, n: int) -> int:
        arr = [1,3,6,10,15,21,28]
        
        if n <= 7:
            return arr[n-1]
        
        def calc(fre):
            total = 0
            x = 7
            for i in range(fre):
                total += x
                x += 7
            return total

        
        k = (n // 7)
        var = (arr[-1] * k) + calc(k-1)
        
        if n % 7 == 0:
            return var

        else:
            rem = n % 7
            return var + arr[rem - 1] + ( n // 7 ) * rem

        


        