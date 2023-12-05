class Solution:
    def numberOfMatches(self, n: int) -> int:
        playes = 0

        while n > 1:
            rem = n % 2
            full = n // 2
            playes += full
            n = full + rem

        return playes
        