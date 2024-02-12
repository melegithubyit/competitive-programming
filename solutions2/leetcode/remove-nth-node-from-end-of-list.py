# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        if length == 1 and n == 1:
            return None

        ele_removed = (length - n) + 1
        if ele_removed == 1:
            head = head.next
            return head
        else:
            counter = 0
            current = head
            while head:
                counter += 1
                if counter == ele_removed - 1:
                    head.next = head.next.next
                    break
                else:
                    head = head.next

        return current

            


