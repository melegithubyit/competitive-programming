class Solution:
    def maxScore(self, cardPoints,k):
        value = len(cardPoints) - k
        total = sum(cardPoints[value:])
        index,answer = 0,total
        while value < len(cardPoints):
            total = total - cardPoints[value] + cardPoints[index]
            answer = max(answer, total)
            value += 1
            index += 1
        return answer

