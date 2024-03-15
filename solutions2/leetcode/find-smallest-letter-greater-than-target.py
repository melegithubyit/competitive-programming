class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l = 0
        r = n - 1
        while l < r:
            m = l + (r - l) // 2
            if letters[m] > target:
                r = m
            else:
                l = m + 1
        
        if letters[l] <= target:
            return letters[0]
        return letters[l]