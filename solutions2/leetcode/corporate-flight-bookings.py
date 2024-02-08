class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n

        for i in bookings:
            first, last, seats = i
            ans[first-1] += seats
            if last <= n - 1:
                ans[last] -= seats

        for i in range(1, n):
            ans[i] += ans[i-1]

        return ans
                    