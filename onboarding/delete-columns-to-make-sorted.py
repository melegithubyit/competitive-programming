class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        temp = []
        for i in strs:
            temp.append(list(i))
        
        counter = 0
        transposed = list(zip(*temp))
        for i in transposed:
            var = sorted(i)
            if list(i) != var:
                counter += 1

        return counter
        