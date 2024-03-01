class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        division = []

        for i in range(1, len(weights)):
            division.append(weights[i] + weights[i-1])
        
        division.sort()

        max_sum = 0
        min_sum = 0

        for i in range(k-1):
            min_sum += division[i]
            max_sum += division[len(division) - i - 1]

        return max_sum - min_sum
