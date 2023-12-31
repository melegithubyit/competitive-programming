class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        n = len(piles)
        score = 0
        iteration = n // 3

        piles.sort(reverse = True)
        counter = 1

        for i in range(iteration):
            score += (piles[i + counter])
            counter += 1

        return score
            

