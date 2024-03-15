class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def isValid(number, piles, hour):
            count = 0
            for i in piles:
                if i % number == 0:
                    count += (i // number)
                else:
                    count += ((i // number) + 1)
            return count <= hour

        low = 1
        high = sum(piles)

        while low < high:
            mid = low + (high - low) // 2
            if isValid(mid, piles, h):
                high = mid
            else:
                low = mid + 1

        return low