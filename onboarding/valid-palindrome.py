class Solution:
    def isPalindrome(self, s: str) -> bool:

        ans = []
        for i in s:
            if i.isalnum():
                ans.append(i.lower())
        
        left = 0
        right = len(ans) - 1

        while left < right:
            if ans[left] != ans[right]:
                return False
            left += 1
            right-= 1
            
        return True
        

