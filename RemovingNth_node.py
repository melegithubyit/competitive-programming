def removeNthFromEnd(head,n):
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    if length == 1 and n == 1:
        return None

    ele_removed = (length - n) + 1
    if ele_removed == 1:
        head = head.next
        return head
    else:
        counter = 0
        current = head
        while head:
            counter += 1
            if counter == ele_removed - 1:
                head.next = head.next.next
                break
            else:
                head = head.next

    return current
