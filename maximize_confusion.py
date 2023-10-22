class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        right = 0
        maxCount = 0
        tCount = 0
        fCount = 0

        while right < len(answerKey):
            if answerKey[right] == 'T':
                tCount += 1
            else:
                fCount += 1
                
            if min(tCount, fCount) > k:
                if answerKey[left] == 'T':
                    tCount -= 1
                else:
                    fCount -= 1
                left += 1

            maxCount = max(maxCount, right - left + 1)
            right += 1

        return maxCount