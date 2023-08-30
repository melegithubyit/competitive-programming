class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[:i] + s[i+1:]:
                return i
            else:
                continue
        return -1
