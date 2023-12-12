class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.lst = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.lst[idKey - 1] = value
        res = []
        while self.ptr < self.n and self.lst[self.ptr] is not None:
            res.append(self.lst[self.ptr])
            self.ptr += 1
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)