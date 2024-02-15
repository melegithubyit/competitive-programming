class Solution:
    def longestPalindrome(self, s: str) -> int:
        store = Counter(s)
        odd_count = 0
        answer = 0

        for i in store:
            if store[i] == 1:
                odd_count += 1
            elif store[i] % 2 == 0:
                answer += store[i]
            else:
                odd_count += 1
                answer += (store[i] - 1)

        if odd_count > 0:
            return answer + 1
        return answer
