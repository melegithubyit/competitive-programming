# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 : return list2
        if not list2 : return list1

        dummy_node = ListNode()
        current = dummy_node

        while list1 and list2:
            val1 = list1.val
            val2 = list2.val
            if val1 < val2:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
            
        if list1 : current.next = list1
        if list2 : current.next = list2
        
        return dummy_node.next