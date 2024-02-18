# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        currA = headA

        while currA:
            lenA += 1
            currA = currA.next

        lenB = 0 
        currB = headB

        while currB:
            lenB += 1
            currB = currB.next

        diff = abs(lenA - lenB)
        
        currA = headA
        currB = headB
        if lenA > lenB:
            for i in range(diff):
                currA = currA.next
        else:
            for i in range(diff):
                currB = currB.next

        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next

        return None

                





