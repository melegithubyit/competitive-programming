class Solution:
    def myPow(self, x , n):
        inital = n
        if n >= 0:
            value1 = n
        else:
            value1 = n * -1

        if value1 == 0:
            return 1

        elif x == 0:
            return 0
        value = self.myPow(x, value1 // 2)
        value *= value
        result = value * x if n % 2 else value

        if inital>=0:
            return result
        else:
            return 1/result

