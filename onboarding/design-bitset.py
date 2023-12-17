class Bitset:

    def __init__(self, size: int):
        
        self.bitset = [0] * size
        self.flipped = [1] * size
        self.one_count = 0

    def fix(self, idx: int) -> None:
        if self.bitset[idx] != 1:
            self.bitset[idx] = 1
            self.flipped[idx] = 0
            self.one_count += 1
        

    def unfix(self, idx: int) -> None:
        if self.bitset[idx] != 0:
            self.bitset[idx] = 0
            self.flipped[idx] = 1
            self.one_count -= 1

        
    def flip(self) -> None:
        self.bitset, self.flipped = self.flipped, self.bitset
        self.one_count = len(self.bitset) - self.one_count
        

    def all(self) -> bool:
        return self.one_count == len(self.bitset)
        

    def one(self) -> bool:
        return self.one_count > 0
        

    def count(self) -> int:
        return self.one_count
        

    def toString(self) -> str:
        res = ''
        for i in self.bitset:
            res += str(i)

        return res
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flipped()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()