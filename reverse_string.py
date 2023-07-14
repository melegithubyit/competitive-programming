class Solution:
    def reverse_string(s) -> None:
        def reverse_helper(left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            reverse_helper(left+1, right-1)
        reverse_helper(0, len(s)-1)
