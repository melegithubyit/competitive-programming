class StockSpanner:
    def __init__(self):
        self.stk = []
        
    def next(self, price: int) -> int:
        span = 1
        while self.stk and self.stk[-1][0] <= price:
            span += self.stk[-1][1]
            self.stk.pop()
        self.stk.append((price, span))
        return span
