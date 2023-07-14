# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            Tval = val1 + val2 + carry
            carry = Tval // 10
            rem = Tval % 10

            current.next = ListNode(rem)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            current.next = ListNode(carry)

        return dummy.next
