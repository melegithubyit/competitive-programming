# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        base_len = length // k
        remainder = length % k
        result = []
        curr = head

        for i in range(k):
            result.append(curr)
            
            for j in range(base_len - 1 + (1 if remainder else 0)):
                if not curr:
                    break
                curr = curr.next

            remainder -= (1 if remainder else 0)

            if curr:
                temp = curr.next
                curr.next = None
                curr = temp
    

        return result

                    
