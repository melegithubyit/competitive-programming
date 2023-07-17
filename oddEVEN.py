# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        result = []
        store = []
        while head:
            store.append(head.val)
            head = head.next

        odd = store[::2]
        even = store[1:][::2]
        total = odd + even

        dummy = ListNode()
        current = dummy

        for i in total:
            current.next = ListNode(i)
            current = current.next

        return dummy.next
