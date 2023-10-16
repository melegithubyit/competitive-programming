class MedianFinder:
    def __init__(self):
        self.smaller = []  
        self.larger = []   

    def addNum(self, num: int) -> None:
        if not self.smaller or num < -self.smaller[0]:
            heappush(self.smaller, -num)
        else:
            heappush(self.larger, num)

        if len(self.smaller) > len(self.larger) + 1:
            heappush(self.larger, -heappop(self.smaller))
        elif len(self.smaller) < len(self.larger):
            heappush(self.smaller, -heappop(self.larger))

    def findMedian(self) -> float:
        if len(self.smaller) == len(self.larger):
            return (-self.smaller[0] + self.larger[0]) / 2.0
        else:
            return float(-self.smaller[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()