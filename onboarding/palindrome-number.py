class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        lst = []
        while x > 0:
            rem = x % 10
            lst.append(rem)
            x //= 10

        left = 0
        right = len(lst) - 1

        while left < right:
            if lst[left] != lst[right]:
                return False
            
            left += 1
            right -= 1

        return True


        