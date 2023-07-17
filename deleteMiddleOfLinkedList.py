# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):
        counter = 0
        curr = head
        while curr:
            counter += 1
            curr = curr.next
        if counter == 1:
            return None

        mid = counter // 2
        current = head
        count = 0

        while head:
            count += 1
            if count == mid:
                head.next = head.next.next
                return current
            head = head.next
