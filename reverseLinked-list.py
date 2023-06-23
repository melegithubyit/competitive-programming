class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        titles = []
        while head:
            titles.append(head.val)
            head = head.next
        computed = titles[:left-1] + \
            (titles[left-1:right])[::-1] + titles[right:]

        dummy = ListNode()
        current = dummy
        for i in computed:
            newNode = ListNode(i)
            current.next = newNode
            current = current.next
        return dummy.next
