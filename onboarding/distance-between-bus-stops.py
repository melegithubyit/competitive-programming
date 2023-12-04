class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        front_sum = 0
        back_sum = 0
        
        if start <= destination:
            for i in range(start, destination):
                front_sum += distance[i]
        
            back_sum = sum(distance)- front_sum
            return min(front_sum, back_sum)

        else:
            for i in range(destination, start):
                front_sum += distance[i]

            back_sum = sum(distance) - front_sum
            return min(front_sum, back_sum)


        