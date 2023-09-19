from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def hasCycle(head: Optional[ListNode]) -> bool:
    s = ListNode()
    s.next = head
    f = ListNode()
    f.next = head

    while s is not None and f is not None:
        if s is f:
            return True

        s = s.next
        if f.next:
            f = f.next.next
        else:
            return False

    return False