class FrequencyTracker:

    def __init__(self):
        self.tracker = defaultdict(int)
        self.frequency = defaultdict(int)

    def add(self, number: int) -> None:
        if self.tracker[number] in self.frequency:
            self.frequency[self.tracker[number]] -= 1
            if self.frequency[self.tracker[number]] == 0:
                del self.frequency[self.tracker[number]]
        self.tracker[number]+=1
        self.frequency[self.tracker[number]] += 1


    def deleteOne(self, number: int) -> None:
        if self.tracker[number] != 0:
            self.frequency[self.tracker[number]] -= 1
            self.tracker[number]-=1
            self.frequency[self.tracker[number]] += 1


    def hasFrequency(self, freq: int) -> bool:
        if self.frequency[freq] > 0:
            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)