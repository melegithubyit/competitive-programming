class Solution:
    def maxScore(self, s: str) -> int:
        total = 0
        for i in s:
            total += int(i)
        max_result = float('-inf')
        left_sum = 0
        right_sum = total

        for i in range(0, len(s) - 1):
            if s[i] == '0':
                left_sum += 1
            else:
                right_sum -= 1

            max_result = max(max_result, left_sum + right_sum)
    
        return max_result

        