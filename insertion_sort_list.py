# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head):
        sorted_head = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = None
            if not sorted_head or curr.val < sorted_head.val:
                curr.next = sorted_head
                sorted_head = curr
            else:
                prev = None
                node = sorted_head
                while node and curr.val >= node.val:
                    prev = node
                    node = node.next
                prev.next = curr
                curr.next = node
            curr = next_node
        return sorted_head
