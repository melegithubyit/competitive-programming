class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        arrows = [points[0]]

        for i in range(1, len(points)):
            x_st, x_en = points[i]
            if x_st <= arrows[-1][1]:
                arrows[-1][0] = x_st
                arrows[-1][1] = min(x_en, arrows[-1][1])
            else:
                arrows.append(points[i])

        return len(arrows)


        