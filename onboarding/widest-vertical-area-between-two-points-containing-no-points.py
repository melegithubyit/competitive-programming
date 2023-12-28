class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        max_width = float('-inf')

        for i in range(1, len(points)):
            prevX, prevY = points[i-1]
            currX, currY = points[i]

            max_width = max(max_width, currX - prevX)
    
        return max_width

        