class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_map = {}
        max_len = 0
        start = 0

        for end in range(n):
            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1
            char_map[s[end]] = end
            max_len = max(max_len, end - start + 1)

        return max_len
