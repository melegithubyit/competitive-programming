class UndergroundSystem:
    def __init__(self):
        self.customers = {}
        self.averageTimes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.customers[id]
        if (startStation, stationName) not in self.averageTimes:
            self.averageTimes[(startStation, stationName)] = [t - startTime, 1]
        else:
            self.averageTimes[(startStation, stationName)][0] += t - startTime
            self.averageTimes[(startStation, stationName)][1] += 1
        del self.customers[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.averageTimes[(startStation, endStation)]
        return total_time / count