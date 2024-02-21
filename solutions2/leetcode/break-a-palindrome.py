class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        splitted = list(palindrome)
        # print(splitted)
        left = 0
        right = len(splitted) - 1

        while left <= right and splitted[left] == 'a':
            left += 1
            right -= 1
        # print(left, right)
        if left >= right:
            splitted[-1] = 'b'
        else:
            splitted[left] = 'a'

        return ''.join(splitted)
