# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(head):
        curr = head
        counter = 0
        while curr:
            counter += 1
            curr = curr.next

        mid = (counter // 2) + 1
        while head:
            mid -= 1
            if mid == 0:
                return head
            else:
                head = head.next
