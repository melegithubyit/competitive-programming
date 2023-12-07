class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        min_val = 0
        max_val = float('-inf')
        for i in ranges:
            s, e = i
            min_val = min(min_val, s)
            max_val = max(max_val, e)
        if right > max_val:
            return False
        
        new = [0] * (max_val - min_val + 1)
        for i in ranges:
            s, e = i
            new[s] += 1
            if e + 1 < len(new):
                new[e+1] -= 1
            
        for i in range(1, len(new)):
            new[i] += new[i-1]
        
        for i in range(left, right + 1):
            if new[i] == 0:
                return False

        return True





        