from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if head is None:
        return None
    if head.next is None:
        return None
    # count the number of node
    flag = head
    count = 0
    while flag is not None:
        flag = flag.next
        count += 1

    # split the list into 2 halves, 1st halves longer
    s = head
    if count % 2 == 0:
        for _ in range(count // 2):
            s = s.next
    else:
        for _ in range(count // 2 + 1):
            s = s.next

    # reverse the second half
    tmp = None
    h = s
    t = s.next
    while t is not None:
        h.next = tmp
        tmp = h
        h = t
        t = t.next
    h.next = tmp

    s = head
    s1 = head.next
    b = h
    b1 = h.next

    # merge 2 halves

    while b1 is not None and s1 is not None:
        s.next = b
        b.next = s1
        s = s1
        b = b1
        s1 = s1.next
        b1 = b1.next
    s.next = b

    if s1 is not None:
        b.next = s1
        s1.next = None