# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        building = []
        while head:
            building.append(head.val)
            head = head.next

        new = [i for i in building if i<x]
        latest = [i for i in building if i not in new]

        final = new + latest
        dummy = ListNode()
        current = dummy

        for i in final:
            newNode = ListNode(i)
            current.next = newNode
            current = current.next

        return dummy.next


