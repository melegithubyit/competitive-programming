# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        start = head

        nums = []
        while (start):
            nums.append(start.val)
            start = start.next
        nums.sort()

        newnums = ListNode()
        x = newnums
        for i in nums:
            x.next = ListNode(i)
            x = x.next
        return newnums.next
