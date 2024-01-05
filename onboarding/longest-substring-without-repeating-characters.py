class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left = 0
        right = 0

        unique = set()

        while right < len(s):

            while left < right and s[right] in unique:
                unique.remove(s[left])
                left += 1

            unique.add(s[right])
            length = max(length, right - left + 1)
            right += 1

        return length

        