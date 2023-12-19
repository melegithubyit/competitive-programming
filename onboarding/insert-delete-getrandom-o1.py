class RandomizedSet:

    def __init__(self):
        self.container = set()
        self.length = 0

    def insert(self, val: int) -> bool:
        if val not in self.container:
            self.container.add(val)
            self.length += 1
            return True

        return False
        

    def remove(self, val: int) -> bool:
        if val in self.container:
            self.container.remove(val)
            self.length -= 1
            return True

        return False
        

    def getRandom(self) -> int:
        lst = list(self.container)
        idx = random.randrange(self.length)
        return lst[idx]

        # return val
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()