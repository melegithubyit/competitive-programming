class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            rem = n % 3
            if rem not in [0,1]:
                return False
            n //= 3

        return True

