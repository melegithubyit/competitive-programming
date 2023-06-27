class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1 or n == 3:
            return True
        if n < 1 or n % 3 != 0:
            return False
        return self.isPowerOfFour(n/3)
