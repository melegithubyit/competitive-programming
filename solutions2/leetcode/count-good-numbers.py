class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7 
        even_count = pow(5, (n + 1) // 2, MOD) 
        odd_count = pow(4, n // 2, MOD) 
    
        return (even_count * odd_count) % MOD