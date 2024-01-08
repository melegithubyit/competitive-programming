class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        max_count = 0
        for i in range(k):
            if s[i] in vowels:
                max_count += 1

        left = 0
        curr_max = max_count

        for right in range(k, len(s)):
            if s[right] in vowels:
                curr_max += 1
            if s[left] in vowels:
                curr_max -= 1
            
            max_count = max(max_count, curr_max)
            left += 1
        
        return max_count


        

        