class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        res = 0
        max_val = flips[0]

        for i in range(1, len(flips) + 1):
            max_val = max(max_val, flips[i-1])
            if i == max_val:
                res += 1
            

        return res
