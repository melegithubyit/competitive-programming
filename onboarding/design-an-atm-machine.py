class ATM:

    def __init__(self):
        self.ATM = [0] * 5
        self.values = [20,50,100,200,500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.ATM[i] += banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:
        total = 0
        res = [0] * 5

        for i in range(4, -1, -1):
            min_val = min(self.ATM[i], amount // self.values[i])
            res[i] = min_val
            total += min_val * self.values[i]
            amount -= min_val * self.values[i]

        if amount != 0:
            return [-1]
        
        for i in range(5):
            self.ATM[i] -= res[i]

        return res





        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)