# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(head):
        test = list()
        track = dict()
        while head:
            test.append(head.val)
            head = head.next

        for i in test:
            track[i] = track.get(i, 0) + 1

        new_test = [num for num in track if track[num] == 1]
        dummy = ListNode()
        current = dummy

        for value in new_test:
            newNode = ListNode(value)
            current.next = newNode
            current = current.next

        return dummy.next
