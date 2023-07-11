# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(head):
        stack = []
        result = []
        index = 0
        current = head
        while current:
            result.append(0)
            while stack and stack[-1][1] < current.val:
                idx, _ = stack.pop()
                result[idx] = current.val

            stack.append((index, current.val))
            current = current.next
            index += 1

        return result
