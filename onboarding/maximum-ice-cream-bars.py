class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        pointer = len(costs) - 1
        total = sum(costs)

        if total <= coins:
            return len(costs)

        for i in range(len(costs)):
            total -= costs[pointer]
            pointer -= 1
            if total <= coins:
                return pointer + 1

        return 0





        