# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(head, k):
        building = []
        while head:
            building.append(head.val)
            head = head.next
        building = building
        if len(building) == 0:
            return None
        else:
            if k > len(building):
                rem = k % len(building)
                for _ in range(rem):
                    if len(building) != 0:
                        value = building.pop()
                        building.insert(0, value)

            elif k < len(building):
                for _ in range(k):
                    if len(building) != 0:
                        value = building.pop()
                        building.insert(0, value)

        dummy = ListNode()
        current = dummy

        for node in building:
            new_node = ListNode(node)
            current.next = new_node
            current = current.next

        return dummy.next
