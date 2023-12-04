class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0

        for i in range(1, len(points)):
            valx, valy = points[i]
            valxp, valyp = points[i-1]
            ans += max(abs(valx - valxp), abs(valy - valyp))

        return ans

        