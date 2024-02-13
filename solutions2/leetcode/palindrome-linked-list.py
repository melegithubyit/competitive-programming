# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse_list(head):
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        original = head
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if length % 2 == 0:
            rev = reverse_list(slow)
        else:
            rev = reverse_list(slow.next)
        
        while rev:
            if original.val != rev.val:
                return False
            original = original.next
            rev = rev.next

        return True



        


        
        