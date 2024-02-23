class Solution:
    def myPow(self, x , n):
        
        if n == 0:
            return 1


        if n < 0:
            x = 1 / x
            n = abs(n)
        a = self.myPow(x, n // 2)

        if n % 2 == 0:
            return a * a
        
        if n % 2 == 1:
            return x * a * a
            

    