class Solution:
    def isHappy(self, n: int) -> bool:

        store = set()
        store.add(n)


        while 1:
            total = 0
            rem = n % 10
            total += (rem ** 2)
            n //= 10
            while n > 0:
                rem = n % 10
                total += (rem ** 2)
                n //= 10

            if total == 1:
                return True
            if total in store:
                return False

            store.add(total) 
            
            n = total

        
        