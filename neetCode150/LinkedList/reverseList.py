from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    tmp = None
    h = head
    t = head.next
    while t is not None:
        h.next = tmp
        tmp = h
        h = t
        t = t.next
    h.next = tmp
    return h
