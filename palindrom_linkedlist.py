class Solution:
    def isPalindrome(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        i, j = 0, -1
        check = True
        while i < (len(arr)+j):
            if arr[i] != arr[j]:
                check = False
                break
            i += 1
            j -= 1
        return check
