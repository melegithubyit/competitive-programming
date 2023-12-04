class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        front_sum = 0
        back_sum = 0
        a,b = min(start,destination), max(start, destination)

        for i in range(a, b):
            front_sum += distance[i]
    
        back_sum = sum(distance)- front_sum
        return min(front_sum, back_sum)


        