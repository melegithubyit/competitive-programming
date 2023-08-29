from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        result = []
        n = len(s)
        m = len(p)
        p_counter = Counter(p)
        window_counter = Counter(s[:m])

        if window_counter == p_counter:
            result.append(0)

        for i in range(1, n - m + 1):
            left_char = s[i - 1]
            right_char = s[i + m - 1]
            window_counter[left_char] -= 1
            if window_counter[left_char] == 0:
                del window_counter[left_char]
            window_counter[right_char] += 1
            if window_counter == p_counter:
                result.append(i)

        return result
