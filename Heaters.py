import bisect


class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        radius = 0

        for house in houses:
            index = bisect.bisect_left(heaters, house)
            if index == 0:
                radius = max(radius, heaters[0] - house)
            elif index == len(heaters):
                radius = max(radius, house - heaters[-1])
            else:
                radius = max(radius, min(
                    heaters[index] - house, house - heaters[index - 1]))

        return radius
