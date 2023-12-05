class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lst = [0] * len(s)
        for i in range(len(s)):
            lst[indices[i]] = s[i]
        return ''.join(lst) 