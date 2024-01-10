class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        T_count = 0
        F_count = 0

        left = 0
        max_length = float('-inf')

        for right in range(len(answerKey)):
            if answerKey[right] == 'T':
                T_count += 1
            else:
                F_count += 1

            min_count = min(T_count, F_count)
            
            while left <= right and min_count > k:
                if answerKey[left] == 'T':
                    T_count -= 1
                else:
                    F_count -= 1
                min_count = min(T_count, F_count)
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

        