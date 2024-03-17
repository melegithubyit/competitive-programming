class TimeMap:

    def __init__(self):
        self.store = {}
        self.words = defaultdict(list)

    def binary_search(self, arr, number):
        index = bisect.bisect_right(arr, number)
        if index == 0:
            return ""
        return arr[index - 1]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[(key, timestamp)] = value
        bisect.insort_left(self.words[key], timestamp)

    def get(self, key: str, timestamp: int) -> str:
        num = self.binary_search(self.words[key], timestamp)
        if num == "":
            return ""
        else:
            return self.store[(key, num)]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)