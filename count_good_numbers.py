class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_count = pow(5, (n + 1) // 2, int(1e9 + 7))
        odd_count = pow(4, n // 2, int(1e9 + 7))

        return (even_count * odd_count) % int(1e9 + 7)
