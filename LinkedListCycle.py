# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if not head or not head.next:
            return False
        first = head
        second = head.next
        while first != second:
            if not second or not second.next:
                return False
            first = first.next
            second = second.next.next
        return True
