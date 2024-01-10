class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        total = sum(cardPoints)
        n = len(cardPoints)
        window_size = n - k

        left = 0

        curr_sum = sum(cardPoints[:window_size])
        curr_max = total - curr_sum
        max_value = curr_max

        for right in range(window_size, n):
            curr_sum += cardPoints[right]
            curr_sum -= cardPoints[left]
            curr_max = total - curr_sum
            max_value = max(max_value, curr_max)
            left += 1

        return max_value






        