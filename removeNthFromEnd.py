# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m = head
        k = head
        while n > 0:
            k = k.next
            n -= 1
        while k and k.next:
            m = m.next
            k = k.next
        if not k:
            head = head.next
        elif m.next:
            m.next = m.next.next
        else:
            head = None
        return head
