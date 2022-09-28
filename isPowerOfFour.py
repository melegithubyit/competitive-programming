class Solution(object):
    def isPowerOfFour(self, n):
        if n==4 or n==1:
            return True
        elif n<=0 or n%4!=0:
            return False
        return self.isPowerOfFour(n/4)
