class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        total = 0
        for idx, ele in enumerate(tickets):
            if idx <= k:
                total += min(ele, tickets[k])
            else:
                total += min(ele, tickets[k] - 1)

        return total
            
        



            


