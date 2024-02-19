# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        flag = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                flag = True
                break
        curr_slow = slow
        curr_fast = head
    
        if flag:
            while curr_slow and curr_fast:
                if curr_slow == curr_fast:
                    return curr_slow

                curr_slow = curr_slow.next
                curr_fast = curr_fast.next

                
        else:
            return 

        