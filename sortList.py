class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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