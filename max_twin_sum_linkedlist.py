# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head) -> int:
        trace = []
        current = head
        counter = 0
        while current:
            counter += 1
            trace.append(current.val)
            current = current.next
        iteration = counter // 2
        first = trace[:iteration]
        second = trace[iteration:][::-1]
        count = 0
        for i in range(iteration):
            val1 = first[i]
            val2 = second[i]
            if val1 + val2 > count:
                count = val1 + val2
        return count


