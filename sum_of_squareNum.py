import math
class Solution:
    def judgeSquareSum(c: int) -> bool:
        left = 0
        right = math.sqrt(c)
        while left <= right:
            summation = left ** 2 + right ** 2
            if summation > c:
                right -= 1
            elif summation < c:
                left += 1
            else:
                return True

        return False


