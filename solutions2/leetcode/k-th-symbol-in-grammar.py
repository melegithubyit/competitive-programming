class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def helper(n, k):

            if n == 1:
                return 0
            
            elif k % 2 == 0:
                number = helper(n-1, math.ceil(k/2))
                return 0 if number == 1 else 1
            
            else:
                return helper(n-1, math.ceil(k/2))
        
        return helper(n, k)

