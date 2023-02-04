class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        value1=head
        value2=head
        while(value2 and value2.next):
            value1=value1.next
            value2=value2.next.next
        return value1